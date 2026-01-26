import os

class ShaderLoader:
    @staticmethod
    def load_shader(ctx, vertex_path, fragment_path):
        """
        Loads shader source code from files and returns a compiled program.
        
        Args:
            ctx: ModernGL context
            vertex_path (str): Path to the vertex shader file
            fragment_path (str): Path to the fragment shader file
            
        Returns:
            The compiled ModernGL program
        """
        # Read Vertex Shader
        with open(vertex_path, 'r') as f:
            vertex_src = f.read()

        # Read Fragment Shader
        with open(fragment_path, 'r') as f:
            fragment_src = f.read()

        # Create and return the program
        # ModernGL handles compilation validation automatically
        program = ctx.program(vertex_shader=vertex_src, fragment_shader=fragment_src)
        return program
