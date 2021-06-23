import sys

sys.path.append('D:\OneDrive - BUas\MGT\Scripts\SwatchM8')

from swatchM8.core import Main

main = Main.Main(GUI=False)

# main.loadData(r"D:\OneDrive - BUas\MGT\Scripts\swatchM8\testFiles\codeTest\TextureName.json")

main.createTexture("CLIDEBUG", r"D:\OneDrive - BUas\MGT\Scripts\SwatchM8\testFiles\codeTest", 128, 8)

# main.app.selectFromCoordinate([0, 0], 8)

# swatch = main.createSwatch("SwatchName", [0, 255, 0])
swatch = main.texture.createSwatch("rood", [0, 255, 0])
# swatch = main.texture.createSwatch("rood", [0, 255, 0])
# swatch = main.createSwatch("SwatchName", [0, 255, 0], ("mario", "petje"))

model = main.createModel('mario')
model = main.createModel('mario2')
model = main.createModel('mario3')
model = main.createModel('mario4')
model = main.createModel('mario5')
model = main.createModel('mario6')
model = main.createModel('mario7')
model = main.createModel('mario8')
model = main.createModel('mario9')
model = main.createModel('mario10')
model = main.createModel('mario11')

# main.addPartToSwatch(swatch, model, 'petje')
# main.addPartToSwatch(swatch, model, 'petje')

# part = main.addPartToSwatch(swatch, model, 'Pet')


# main.deletePart(swatch, part)

# swatch = main.createSwatch("swatchName", [0, 255, 0])
# swatch02 = main.createSwatch("swatchName02", [255, 0, 0])

# model = main.getModelByName('ModelName69')
# main.deleteModel(model)
# for i in main.models:
#     print(i.name)


# for i in main.models:
#
#     print i.name
#
#     for j in i.parts:
#
#         print j.name
#         print j.swatch.name


# swatch = main.texture.getSwatchByName("HatMario")
# model = main.createModel("Bowser")
# part = model.addPart("Bower Eye")
# swatch.addPart(part)
# for i in main.activeTexture.getSwatchByName("SwatchName03").parts:
#     print i.name

# for i in range(main.texture.amountOfSwatchesOnRow):
#     for j in range(main.texture.amountOfSwatchesOnRow):
#
#         print main.texture.availableCoordinates[i][j]

# main.saveData()

# if isinstance(obj, Swatch.Swatch):
