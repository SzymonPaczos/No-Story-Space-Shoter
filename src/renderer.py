import moderngl
import numpy as np
import pygame
import os
from src.shader_loader import ShaderLoader

class Renderer:
    def __init__(self, screen_size):
        """
        Initializes the ModernGL rendering context.
        
        Args:
            screen_size (tuple): (width, height) of the window.
        """
        # 1. Detect existing OpenGL context created by Pygame
        self.ctx = moderngl.create_context()
        
        # 2. Enable Blending (Alpha Transparency)
        # This is crucial for sprites with transparent backgrounds (PNGs)
        self.ctx.enable(moderngl.BLEND)
        self.ctx.blend_func = moderngl.SRC_ALPHA, moderngl.ONE_MINUS_SRC_ALPHA
        
        # 3. Load Shaders
        # We process the raw shader files into a GPU program
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.program = ShaderLoader.load_shader(
            self.ctx,
            os.path.join(base_path, 'shaders/default.vert'),
            os.path.join(base_path, 'shaders/default.frag')
        )
        
        # 4. Create Geometry (A reusable Quad)
        # We only need ONE square in memory. We will draw it multiple times
        # in different places (using matrices).
        # Data format: x, y (position 0..1), u, v (texture coords 0..1)
        # Used as a Triangle Strip (Z pattern)
        vertices = np.array([
            # x, y,   u, v
            0.0, 0.0, 0.0, 0.0,
            1.0, 0.0, 1.0, 0.0,
            0.0, 1.0, 0.0, 1.0,
            1.0, 1.0, 1.0, 1.0,
        ], dtype='f4')
        
        self.vbo = self.ctx.buffer(vertices.tobytes())
        
        # VAO describing the buffer layout to the shader:
        # '2f 2f' means: 2 floats for Position, 2 floats for TexCoord
        self.vao = self.ctx.vertex_array(
            self.program,
            [
                (self.vbo, '2f 2f', 'in_vert', 'in_texcoord'),
            ]
        )
        
        # 5. Setup Projection Matrix
        # Orthographic Projection mimics 2D screen coordinates.
        # (0,0) Top-Left, (800,600) Bottom-Right.
        self.screen_size = screen_size
        self.update_projection()

    def update_projection(self):
        width, height = self.screen_size
        # Equivalent to: glOrtho(0, width, height, 0, -1, 1)
        # We construct the matrix manually for ModernGL.
        self.projection = self.create_ortho_matrix(0, width, height, 0, -1.0, 1.0)
        self.program['projection'].write(self.projection.tobytes())

    def create_ortho_matrix(self, left, right, bottom, top, near, far):
        """Creates an Orthographic Projection Matrix (Column-Major)"""
        rml = right - left
        tmb = top - bottom
        fmn = far - near
        
        mat = np.array([
            [2.0/rml, 0.0, 0.0, 0.0],
            [0.0, 2.0/tmb, 0.0, 0.0],
            [0.0, 0.0, -2.0/fmn, 0.0],
            [-(right+left)/rml, -(top+bottom)/tmb, -(far+near)/fmn, 1.0]
        ], dtype='f4')
        return mat

    def create_transform_matrix(self, x, y, width, height, rotation=0):
        """
        Creates a Model Matrix combining Translation and Scale.
        Order: Scale -> Translate
        """
        sq_scale = np.array([
            [width, 0.0, 0.0, 0.0],
            [0.0, height, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ], dtype='f4')

        sq_trans = np.array([
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [x, y, 0.0, 1.0]
        ], dtype='f4')
        
        # Matrix multiplication (numpy uses @ or matmul)
        return sq_scale @ sq_trans

    def clear(self):
        """Clears the screen (GPU framebuffer)"""
        self.ctx.clear(0.0, 0.0, 0.2) # Deep Blue space color

    def draw(self, texture, position, size=None):
        """
        Draws a texture at specific position.
        
        Args:
            texture: ModernGL Texture object
            position: (x, y) tuple
            size: (width, height) tuple. If None, uses texture size.
        """
        if size is None:
            size = (texture.width, texture.height)

        # Bind the texture to texture unit 0
        texture.use(location=0)
        
        # Create transform matrix
        model_mat = self.create_transform_matrix(position[0], position[1], size[0], size[1])
        
        # Upload matrix to GPU
        self.program['model'].write(model_mat.tobytes())
        
        # Execute Draw Call
        self.vao.render(moderngl.TRIANGLE_STRIP)

    def texture_from_surface(self, surface):
        """Converts a Pygame Surface to a ModernGL Texture"""
        texture = self.ctx.texture(surface.get_size(), 4, pygame.image.tostring(surface, 'RGBA'))
        return texture
