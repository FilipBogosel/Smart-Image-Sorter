#This module contains the configuration settings for the Smart Image Sorter application.
# ========== CONFIGURATION ========== #
SOURCE_FOLDER = "D:\\Github\\Smart-Image-Sorter\\test_photos"
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
DESTINATION_FOLDERS = {
    'portrait': "Portrait",# portrait = 1 person
    'couple': "Couple",# couple = 2 people
    'group': "Group",# group = 3+ people
    'nature': "Nature",# nature = nature photos, but not with people
    'urban': "Urban",# urban = cityscape, buildings, etc.
    'food': "Food",# food = food photos
    'art': "Art",# art = paintings, sculptures, etc.
    'vehicle': "Vehicle",# vehicle = cars, bikes, etc.
    'pet': "Pet",# pet = photo with animals, but not in nature, so if it does not find any keyword in the nature
    # category, but it finds a keyword for an animal, it will be classified as a pet
    'non_photos': "Non_Photos",# non_photos = non-image files
    'other': "Other_Photos"# other = images that don't fit the above categories
}

NATURE_KEYWORDS = {
    'tree', 'flower', 'mountain', 'forest', 'river', 'valley', 'field', 'lake',
    'ocean', 'sky', 'cloud', 'sunset', 'waterfall', 'leaf', 'plant', 'grass','bush','cactus',
    'desert','beach','sand','rock','cave','volcano','island','jungle','rainforest','savanna',
    'tundra','arctic','antarctic','glacier','wetland','marsh','swamp','mangrove','reef','coral',
    'sea','seashore','shore','coast','cliff','canyon','hill','valley','plateau','mesa'
}#keywords that can be found in nature photos when they are analyzed by the ResNet18 model

URBAN_KEYWORDS = {
    'city', 'town', 'village', 'street', 'road', 'building', 'house', 'apartment', 'skyscraper',
    'office', 'store', 'shop', 'restaurant', 'cafe', 'hotel', 'motel', 'parking', 'station',
    'airport', 'harbor', 'port', 'bridge', 'tunnel', 'plaza', 'square', 'market', 'mall', 'cinema',
    'theater', 'museum', 'library', 'school', 'college', 'university', 'hospital', 'clinic', 'police',
    'fire', 'post', 'office', 'bank', 'church', 'temple', 'mosque', 'synagogue', 'stadium',
    'arena', 'court', 'field', 'park', 'garden', 'zoo', 'aquarium', 'amusement', 'playground','fountain'
}#keywords that can be found in urban photos when they are analyzed by the ResNet18 model

FOOD_KEYWORDS = {
    'food', 'meal', 'dish', 'plate', 'breakfast', 'lunch', 'dinner', 'snack', 'dessert', 'fruit',
    'vegetable', 'bread', 'cake', 'pie', 'cookie', 'candy', 'chocolate', 'ice cream', 'pizza',
    'pasta', 'burger', 'sandwich', 'taco', 'sushi', 'salad', 'soup', 'stew', 'curry', 'rice',
    'noodle', 'meat', 'beef', 'pork', 'chicken', 'fish', 'seafood', 'egg', 'cheese', 'milk',
    'coffee', 'tea', 'juice', 'soda', 'beer', 'wine', 'liquor', 'water'
}  # keywords that can be found in food photos when they are analyzed by the ResNet18 model

ART_KEYWORDS = {
    'art', 'painting', 'drawing', 'sketch', 'sculpture', 'statue', 'carving', 'pottery', 'ceramic',
    'glass', 'metal', 'wood', 'stone', 'bronze', 'marble', 'canvas', 'paper', 'ink', 'pencil',
    'brush', 'palette', 'easel', 'frame', 'gallery', 'museum', 'exhibit', 'show', 'artist',
    'painter', 'sculptor', 'potter', 'ceramicist', 'glassblower', 'metalworker', 'woodworker',
    'bronze', 'artwork', 'masterpiece', 'portrait', 'landscape'
}  # keywords that can be found in art photos when they are analyzed by the ResNet18 model

VEHICLE_KEYWORDS = {
    'vehicle', 'car', 'truck', 'van', 'bus', 'motorcycle', 'bike', 'bicycle', 'scooter', 'moped',
    'boat', 'ship', 'yacht', 'sailboat', 'cruise', 'submarine', 'airplane', 'helicopter', 'jet',
    'rocket', 'train', 'tram', 'subway', 'taxi', 'cab', 'limo', 'bus', 'trolley', 'tractor',
    'bulldozer', 'crane', 'forklift', 'excavator', 'dump', 'truck', 'garbage', 'truck', 'fire',
    'sport car', 'sedan', 'hatchback', 'coupe', 'convertible', 'suv', 'minivan', 'pickup', 'exhaust'
}  # keywords that can be found in vehicle photos when they are analyzed by the ResNet18 model


ANIMAL_KEYWORDS = {
    'animal', 'mammal', 'reptile', 'bird', 'fish', 'insect', 'amphibian', 'arachnid', 'crustacean',
    'mollusk', 'worm', 'snail', 'slug', 'jellyfish', 'octopus', 'squid', 'starfish', 'sea urchin',
    'coral', 'anemone', 'sponge', 'crab', 'lobster', 'shrimp', 'prawn', 'barnacle', 'insect', 'ant',
    'bee', 'wasp', 'hornet', 'fly', 'mosquito', 'moth', 'butterfly', 'beetle', 'bug', 'grasshopper',
    'dog', 'cat', 'horse', 'cow', 'pig', 'sheep', 'goat', 'chicken', 'duck', 'goose', 'turkey',
    'rabbit', 'hamster', 'guinea pig', 'ferret', 'rat', 'mouse', 'squirrel', 'chipmunk', 'beaver',
    'otter', 'seal', 'walrus', 'whale', 'dolphin', 'porpoise', 'shark', 'ray', 'eel', 'snake',
    'lizard', 'gecko', 'iguana', 'turtle', 'tortoise', 'crocodile', 'alligator', 'frog', 'toad',
    'newt', 'salamander', 'axolotl', 'parrot', 'cockatoo', 'macaw', 'budgie', 'canary', 'finch',
    'sparrow', 'crow', 'raven', 'magpie', 'jay', 'pigeon', 'dove', 'vulture', 'hawk', 'eagle',
    'falcon', 'owl', 'kingfisher', 'woodpecker', 'hummingbird', 'swift', 'swallow', 'martin'
}#keywords that can be found in animal photos when they are analyzed by the ResNet18 model