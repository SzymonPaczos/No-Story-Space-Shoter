#version 330 core

// Input from vertex shader
in vec2 v_texcoord;

// Uniforms
uniform sampler2D Texture; // The sprite image

// Output color
out vec4 f_color;

void main() {
    // Sample the color from the texture at the given coordinate
    f_color = texture(Texture, v_texcoord);
}
