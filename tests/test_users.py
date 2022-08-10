from flask import Flask
import json
from pip import main
from main import Contact, Posts, post

def test_new_contact():
    contact = Contact('first post', 1234567891, 'first post', 'firstpost@gmail.com')
    assert contact.name == 'first post'
    assert contact.phone_num == '1234567891'
    assert contact.msg == 'first post'
    assert contact.email == 'firstpost@gmail.com'
    


def test_new_post():
    post = Posts('first post', 'first-post', 'This is my first post', 'My tagline')
    assert Posts.title == 'first post'
    assert Posts.slug == 'first-post'
    assert Posts.content == 'This is my first post'
    assert Posts.tagline == 'My tagline'