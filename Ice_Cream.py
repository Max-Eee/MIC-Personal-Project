from flask import Flask, request, jsonify

app = Flask(__name__)

flavors = {
    'vanilla': ['milk', 'cream', 'sugar', 'vanilla extract'],
    'chocolate': ['milk', 'cream', 'sugar', 'cocoa powder'],
    'strawberry': ['milk', 'cream', 'sugar', 'strawberry puree'],
    'mint_chip': ['milk', 'cream', 'sugar', 'mint extract', 'chocolate chips'],
    'cookies_and_cream': ['milk', 'cream', 'sugar', 'cookie crumbs'],
    'rocky_road': ['milk', 'cream', 'sugar', 'marshmallows', 'nuts', 'chocolate chunks'],
    'coffee': ['milk', 'cream', 'sugar', 'instant coffee'],
    'pistachio': ['milk', 'cream', 'sugar', 'pistachio paste'],
    'rainbow_sherbet': ['milk', 'sugar', 'fruit purees', 'food coloring'],
    'cotton_candy': ['milk', 'cream', 'sugar', 'cotton candy flavoring', 'rainbow sprinkles'],
}

@app.route('/')
def index():
    return 'Welcome to the Ice Cream Mixer!'

@app.route('/ice_cream')
def get_ice_cream():
    ice_cream_name = request.args.get('name')
    ingredients = flavors.get(ice_cream_name, [])
    if ingredients:
        return jsonify({'ingredients': ingredients})
    else:
        return jsonify({'error': 'Ice cream not found'}), 404

@app.route('/update_flavors', methods=['POST'])
def update_flavors():
    if request.json:
        if 'admin_key' in request.json and 'flavor' in request.json and 'ingredients' in request.json:
            admin_key = request.json['admin_key']
            if admin_key == 'fiZazaeBwX2ul9nh':
                flavor = request.json['flavor']
                ingredients = request.json['ingredients']
                flavors[flavor] = ingredients
                return jsonify({'message': f'Flavor {flavor} updated successfully'})
            else:
                return jsonify({'error': 'Invalid admin key'}), 403
        else:
            return jsonify({'error': 'Missing parameters in request'}), 400
    else:
        return jsonify({'error': 'Invalid JSON body'}), 400

if __name__ == '__main__':
    app.run(debug=True)
