from hypar import glTF
from random import randint, uniform
from typing import List

from aecSpace.aecPoint import aecPoint
from aecSpace.aecShaper import aecShaper
from aecSpace.aecSpace import aecSpace
from aecSpace.aecSpaceGroup import aecSpaceGroup
from aecSpace.aecSpacer import aecSpacer

spacer = aecSpacer()
shaper = aecShaper()

model = glTF()
colorAqua = model.add_material(0.3, 0.72, 0.392, 1.0, 0.8, "Aqua")
colorBlue = model.add_material(0.0, 0.631, 0.945, 1.0, 0.8, "Blue")
colorBrown = model.add_material(0.5, 0.2, 0.0, 1.0, 0.5, "Brown")
colorGray = model.add_material(0.5, 0.5, 0.5, 1.0, 0.8, "Gray")
colorGranite = model.add_material(0.25, 0.25, 0.25, 1.0, 0.8, "Granite")
colorGreen = model.add_material(0.486, 0.733, 0.0, 1.0, 0.8, "Green")
colorOrange = model.add_material(0.964, 0.325, 0.078, 1.0, 0.8, "Orange")
colorPurple = model.add_material(0.75, 0.07, 1.0, 1.0, 0.8, "Purple")
colorSand = model.add_material(1.0, 0.843, 0.376, 1.0, 0.8, "Sand") 
colorSilver = model.add_material(0.75, 0.75, 0.75, 1.0, 1.0, "Silver")
colorWhite = model.add_material(1.0, 1.0, 1.0, 1.0, 0.8, "White")
colorYellow = model.add_material(1.0, 0.733, 0.0, 1.0, 0.8, "Yellow")

def getColor(color: int = 0):
    if color == 0: return colorAqua
    if color == 1: return colorBlue
    if color == 2: return colorBrown
    if color == 3: return colorGray
    if color == 4: return colorGranite
    if color == 5: return colorGreen
    if color == 6: return colorOrange
    if color == 7: return colorPurple
    if color == 8: return colorSand
    if color == 9: return colorSilver
    if color == 10: return colorWhite
    if color == 11: return colorYellow

def makeCheckOut(color: int = 0):
    components = aecSpaceGroup();
    base = aecSpace();
    base.boundary = shaper.makeBox(aecPoint(), 75, 150)
    base.height = 100
    top = aecSpace();
    top.boundary = shaper.makeU(aecPoint(), 
                                xSize = 170, 
                                ySize = 80, 
                                xWidth1 = 20, 
                                xWidth2 = 20, 
                                yDepth = 20)
    top.height = 30
    top.rotate(90)
    top.moveBy(-25, 50, 100)
    components.add([base, top])
    components.moveBy(70, 70)
    color = colorBrown
    for component in components.spaces:
        mesh = component.mesh_graphic
        model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, color)

def makeRackCross(rotation: float, moveBy: List[float]):
    components = aecSpaceGroup();
    base = aecSpace();
    base.boundary = shaper.makeCylinder(aecPoint(), radius = 40)
    base.height = 5
    support = aecSpace()
    support.boundary = shaper.makeCylinder(aecPoint(), radius = 5)
    support.height = 157
    support.moveBy(0, 0, 5)
    top = aecSpace();
    top.boundary = shaper.makeCross(aecPoint(-50, -50), 100, 100, xWidth = 10 , yDepth = 10)
    top.height = 4
    top.moveBy(0, 0, 162)
    components.add([base, support, top])
    components.moveBy(moveBy[0], moveBy[1], moveBy[2])
    components.rotate(uniform(0, rotation), base.center_floor)
    for component in components.spaces:
        mesh = component.mesh_graphic
        model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorSilver)
        
def makeRackRound(color: int, moveBy: List[float]):
    components = aecSpaceGroup();
    base = aecSpace();
    base.boundary = shaper.makeCylinder(radius = 40)
    base.height = 5
    support = aecSpace();
    support.boundary = shaper.makeCylinder(radius = 5)
    support.height = 125
    support.moveBy(0, 0, 5)
    top = aecSpace();
    top.boundary = shaper.makeCylinder(radius = 50)
    top.height = 3
    top.moveBy(0, 0, 130)
    components.add([base, support, top])
    components.moveBy(moveBy[0], moveBy[1])
    color = getColor(color)
    for component in components.spaces:
        mesh = component.mesh_graphic
        model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, color)
        
def makeShelfSingle(rotation: float, color: int, moveBy: List[float]):
    components = aecSpaceGroup();
    base = aecSpace();
    length = 200
    base.boundary = shaper.makeBox(aecPoint(), 50, length)
    base.height = 25
    divider = aecSpace()
    divider.boundary = shaper.makeBox(aecPoint(), 4, length - 10)
    divider.height = 125
    divider.moveTo(fromPnt = aecPoint(), toPnt = aecPoint(0, 5, 25))
    lowShelfFront = aecSpace()
    lowShelfFront.boundary = shaper.makeBox(aecPoint(), 43, length - 10)
    lowShelfFront.height = 2
    lowShelfFront.moveTo(fromPnt = aecPoint(), toPnt = aecPoint(4, 5, 65))
    highShelfFront = spacer.copy(lowShelfFront, 0, 0, 40)
    components.add([base, divider, lowShelfFront, highShelfFront])
    components.rotate(rotation, base.center_floor)
    components.moveBy(moveBy[0], moveBy[1])
    components.rotate(uniform(0, rotation), base.center_floor)
    color = getColor(color)
    for component in components.spaces:
        mesh = component.mesh_graphic
        model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, color)    

def makeShelfDouble(rotation: float, color: int, moveBy: List[float]):
    components = aecSpaceGroup();
    base = aecSpace();
    length = 200
    base.boundary = shaper.makeBox(aecPoint(), 100, length)
    base.height = 25
    divider = aecSpace();
    divider.boundary = shaper.makeBox(aecPoint(), 4, length - 10)
    divider.height = 125
    divider.moveTo(fromPnt = aecPoint(), toPnt = aecPoint(48, 5, 25))
    lowShelfFront = aecSpace();
    lowShelfFront.boundary = shaper.makeBox(aecPoint(), 43, length - 10)
    lowShelfFront.height = 2                     
    lowShelfFront.moveTo(fromPnt = aecPoint(), toPnt = aecPoint(52, 5, 65))
    lowShelfBack = spacer.copy(lowShelfFront)
    lowShelfBack.mirror([aecPoint(50, 0), aecPoint(50, 500)])
    highShelfFront = spacer.copy(lowShelfFront, z = 40)
    highShelfBack = spacer.copy(lowShelfBack, z = 40)
    components.add([base, divider, lowShelfFront, lowShelfBack, highShelfFront, highShelfBack])
    components.moveBy(moveBy[0], moveBy[1])
    components.rotate(uniform(0, rotation), base.center_floor)
    color = getColor(color)
    for component in components.spaces:
        mesh = component.mesh_graphic
        model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, color)    

def makeShelfTiered(rotation: float, color: int, moveBy: List[float]):
    components = aecSpaceGroup();
    lowShelf = aecSpace();  
    lowShelf.boundary = shaper.makeBox(aecPoint(), 100, 150)
    lowShelf.height = 3
    lowShelf.moveBy(z = 27)
    midShelf = spacer.copy(lowShelf, z = 30)
    midShelf.scale(0.75, 0.75, 1)
    topShelf = spacer.copy(midShelf, z = 30)
    topShelf.scale(0.75, 0.75, 1)   
    base = spacer.copy(lowShelf, z = -27)
    base.scale(0.75, 0.75, 9)
    support1 = spacer.copy(base, z = 30)
    support1.scale(0.25, 0.5, 1)
    support1.height = 27
    support2 = spacer.copy(support1, z = 30)
    components.add([base, lowShelf, midShelf, topShelf, support1, support2])
    components.moveBy(moveBy[0], moveBy[1])
    components.rotate(uniform(0, rotation), base.center_floor)
    color = getColor(color)
    for component in components.spaces:
        mesh = component.mesh_graphic
        model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, color)  

def makeRetail(fixTypes: int = 0, fixColor: int = 1, flrColor: int = 0, rotation: float = 45):
    moveBy = [100, 100, 0]
    floor = aecSpace()
    floor.boundary = shaper.makeBox(aecPoint(), 1700, 2100)
    floor.level = -1
    floor.height = 1
    mesh = floor.mesh_graphic
    model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, getColor(flrColor))   
    makeCheckOut(fixColor)
    items = 0
    x = 0
    displace = 350
    while x < 4:
        moveBy[0] += displace
        fixType = randint(0, fixTypes)
        if fixType == 0: 
            makeRackCross(rotation, moveBy) 
            items += 32
        if fixType == 1: 
            makeRackRound(fixColor, moveBy) 
            items += 60
        if fixType == 2: 
            makeShelfSingle(rotation, fixColor, moveBy) 
            items += 25
        if fixType == 3: 
            makeShelfDouble(rotation, fixColor, moveBy) 
            items += 50
        if fixType == 4: 
            makeShelfTiered(rotation, fixColor, moveBy) 
            items += 45       
        x += 1   
    x = 0
    y = 0
    while y < 5:
        moveBy = [100, moveBy[1] + displace, 0]
        while x < 5:
            fixType = randint(0, fixTypes)
            if fixType == 0: 
                makeRackCross(rotation, moveBy) 
                items += 32
            if fixType == 1: 
                makeRackRound(fixColor, moveBy) 
                items += 60
            if fixType == 2: 
                makeShelfSingle(rotation, fixColor, moveBy) 
                items += 25
            if fixType == 3: 
                makeShelfDouble(rotation, fixColor, moveBy) 
                items += 50
            if fixType == 4: 
                makeShelfTiered(rotation, fixColor, moveBy) 
                items += 45
            moveBy[0] = moveBy[0] + displace
            x += 1  
        x = 0
        y += 1   
    return {"model": model.save_base64(), 'computed':{'Total items':items}}   
#    model.save_glb('model.glb')
#
#makeRetail(fixTypes = randint(0, 4), 
#           fixColor = randint(0, 11), 
#           flrColor = randint(0, 11),
#           rotation = 345)


    