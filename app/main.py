from flask import render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.models import post, tag
from app import app, db


@app.route('/')
def index():
  return render_template('http.html')


@app.route('/creat', methods=['POST'])
def creat():
  data = request.get_json()
  title = data.get('title')
  contant = data.get('contant')
  tags = data.get('tags')
  tags = [tag(name=tag_name) for tag_name in tags]
  db.session.add_all(tags)
  db.session.commit()
  p = post(title=title, contant=contant, tags=tags)
  db.session.add(p)
  db.session.commit()

  return jsonify({'message': 'Post created successfully'}), 201


@app.route('/get_post/<int:id>', methods=['GET'])
def get_post_by_id(id):
  p = post.query.get_or_404(id)
  return jsonify({
      'id': p.id,
      'title': p.title,
      'contant': p.contant,
      'tags': [tag.name for tag in p.tags]
  })


@app.route('/update_post/<int:id>', methods=['PUT'])
def update_post(id):
  p = post.query.get_or_404(id)
  data = request.get_json()
  p.title = data.get('title', p.title)
  p.contant = data.get('contant', p.contant)
  p.tags = [tag(name=tag_name) for tag_name in data.get('tags', [])]
  db.session.commit()
  return jsonify({'message': 'Post updated successfully'}), 200


@app.route('/delete_post/<int:id>', methods=['DELETE'])
def delete_post(id):
  p = post.query.get_or_404(id)
  db.session.delete(p)
  db.session.commit()
  return jsonify({'message': 'Post deleted successfully'}), 200


@app.route('/get_tags', methods=['GET'])
def get_tags():
  tags = tag.query.all()
  tag_list = []
  for t in tags:
    tag_list.append({'id': t.id, 'name': t.name})
  return jsonify(tag_list), 200


@app.route('/posts', methods=['GET'])
def get_post():
  posts = post.query.all()
  post_list = []
  for p in posts:
    post_list.append({
        'id': p.id,
        'title': p.title,
        'contant': p.contant,
        'tags': [tag.name for tag in p.tags]
    })
  return jsonify(post_list), 200
