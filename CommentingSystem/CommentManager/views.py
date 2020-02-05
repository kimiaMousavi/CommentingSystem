from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comment, Post
from .serializer import CommentSerializer, PostSerializer


class CommentView(APIView):

    def get(self, request):

        try:
            post_id = Post.objects.get(post_id=request.data['post_id'])
            comments = Comment.objects.filter(post_id=post_id).order_by('-date') # ordered
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

        except KeyError:
            content = {'error': 'post_id needed in body!'}
            return Response(content)
        except ObjectDoesNotExist:
            content = {'error': 'no post with this id'}
            return Response(content)

    def post(self, request):

        try:
            content = dict()
            author = request.data['author']
            text = request.data['text']
            post_id = Post.objects.get(post_id=request.data['post_id'])  # Post.objects.get cho onvar az noe post e
            res = Comment.objects.create(author=author, text=text, post_id=post_id)

            content = {"msg": "comment added!"}
        except KeyError:
            content = {'error': 'post_id,author,text needed in body!'}
        except ObjectDoesNotExist:
            content = {'error': 'no post with this id'}
        except IntegrityError:
            content = {'error': 'a comment exist with this id'}

        return Response(content)

    def put(self, request):

        try:
            author = request.data['author']
            text = request.data['text']
            comment_id = request.data['comment_id']
            post_id = Post.objects.get(post_id=request.data['post_id'])
            obj = Comment.objects.get(author=author, post_id=post_id, pk=comment_id)
            obj.text = text
            obj.save()
            content = {"msg": "comment updated!"}
        except ObjectDoesNotExist:
            content = {'error': 'no post or comment with this id'}
        except KeyError:
            content = {'error': 'post_id, author, text,comment_id needed in body!'}
        return Response(content)

    def delete(self, request):

        content = dict()
        try:
            post_id = Post.objects.get(post_id=request.data['post_id'])
            comment_id = request.data['comment_id']
            obj = Comment.objects.get(post_id=post_id, pk=comment_id)
            obj.delete()
            content = {"msg": "comment deleted!"}

        except KeyError:
            content = {'error': 'post_id and comment_id needed in body!'}

        except ObjectDoesNotExist:
            content = {'error': 'no comment with this id'}
        return Response(content)


class PostView(APIView):

    def get(self,request):


        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):

        content = dict()
        try:
            post_id = request.data['post_id']
            res = Post.objects.create(post_id=post_id)

            if res:
                content = {"msg": "Post added!"}
            else:
                content = {'error': 'error in post creation!'}

        except KeyError:
            content = {'error': 'post_id needed in body!'}

        except ObjectDoesNotExist:
            content = {'error': 'no comment with this id'}
        except IntegrityError:
            content = {'error': 'a post exist with this id'}
        return Response(content)

    def delete(self, request):

        content = dict()
        try:
            post_id = request.data['post_id']
            obj = Post.objects.get(post_id=post_id)
            obj.delete()
            content = {"msg": "post deleted!"}
        except KeyError:
            content = {'error': 'post_id needed in body!'}

        except ObjectDoesNotExist:
            content = {'error': 'no post with this id'}

        return Response(content)
