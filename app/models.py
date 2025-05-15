import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

tags = db.Table(
    'tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
)


class post(db.Model):
  id: so.Mapped[int] = so.mapped_column(primary_key=True)
  title: so.Mapped[str] = so.mapped_column(sa.String(128))
  contant: so.Mapped[str] = so.mapped_column(sa.Text)
  catigory: so.Mapped[str] = so.mapped_column(sa.String(16))
  tags = db.relationship('tag',
                         secondary=tags,
                         backref=db.backref('post', lazy='dynamic'))

  def __repr__(self):
    return f'Post {self.title}  : \n {self.contant}'


class tag(db.Model):
  id: so.Mapped[int] = so.mapped_column(primary_key=True)
  name: so.Mapped[str] = so.mapped_column(sa.String(32))

  def __repr__(self):
    return f'Tag {self.name}'
