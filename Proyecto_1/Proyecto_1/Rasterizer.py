import shaders
from gl import Renderer, Model

# La resolucion de la imagen generada
width = 1920    
height = 1080   


# Inicializar el Renderer con la resolucion definida y color de fondo
rend = Renderer(width, height)
rend.glClearColor(0.2, 0.2, 0.2)

rend.glBackgroundTexture("ocean.bmp")
rend.glClearBackground()

# Se mueve la posicion de la luz
rend.directionalLight = (0,0,-1)


# Se cargan los modelos con sus efectos a renderizar
model1 = Model("modelos/TropicalFish01.obj",
              translate = (-3.8,1.6,-5),                
              rotate = (0,0,0),                    
              scale = (2, 2, 2))
model1.LoadTexture("modelos/TropicalFish01.bmp")
model1.SetShaders(shaders.vertexShader, shaders.tigerShader)
rend.glAddModel(model1)

model2 = Model("modelos/TropicalFish02.obj",
              translate = (-1.5,-1,-5),                
              rotate = (0,-15,0),                    
              scale = (2.7, 2.7, 2.7))
model2.LoadTexture("modelos/TropicalFish02.bmp")
model2.SetShaders(shaders.vertexShader, shaders.gradientShader)
rend.glAddModel(model2)

model3 = Model("modelos/TropicalFish03.obj",
              translate = (1,1.3,-5),                
              rotate = (1.5,25,0),                    
              scale = (1.5, 1.5, 1.5))
model3.LoadTexture("modelos/TropicalFish03.bmp")
model3.SetShaders(shaders.vertexShader, shaders.inverseShader)
rend.glAddModel(model3)

model4 = Model("modelos/TropicalFish04.obj",
              translate = (3.5,-1.6,-5),                
              rotate = (0,0,0),                    
              scale = (3.2, 3.2, 3.2))
model4.LoadTexture("modelos/TropicalFish04.bmp")
model4.SetShaders(shaders.vertexShader, shaders.gridShader)
rend.glAddModel(model4)



# Renderizar el modelo en la imagen
rend.glRender()

# Se crea el FrameBuffer con la imagen renderizada
rend.glFinish("output.bmp")

