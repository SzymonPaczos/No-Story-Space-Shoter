#version 330 core

// Input attributes from the VBO
in vec2 in_vert;
in vec2 in_texcoord;

// Uniforms (Global variables set from Python)
uniform mat4 projection; // Converts pixel coordinates to normalized device coordinates
uniform mat4 model;      // Transforms the object (position, rotation, scale)

// Output to the fragment shader
out vec2 v_texcoord;

void main() {
    v_texcoord = in_texcoord;
    // Apply transformations: Projection * Model * Vertex
    gl_Position = projection * model * vec4(in_vert, 0.0, 1.0);
}
