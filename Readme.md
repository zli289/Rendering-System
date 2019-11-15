#   Rendering System for computer graphics
+   Camera: defines camera parements, Viewing and Perspective translation here.
+   Entrance: loading file, camera configuration, object initializtion, light source setting, loading texture file, choosing shading models.
+   Interpolation: Scan conversion and Z-buffer functions for z values(visible surface), vertex normals(phong shading) and light intensities(ground shading), [u,v] values(texture mapping) on points.
+   Maxtrix Caculation: vectors crossproduct and dotproduct, adding and subtracting calculation, matrix multiplation, vector normalization.
+   Readfile: gets points and polygons from loaded file.
+   Rendering: using thinker API to render by pixels, rgb transformation function.
+   SingleObject: includes object color, [u,v] for texture, points(world, screen, device) and edges, vertex normals and polygon normals, backfaceculling function.
+   Shading: three shading models, illumination function for single vector.
+   Texture: cylinder mapping to get [u,v] for single object, textureimage function to genertate texture image by using perlin noise 


