from django import forms
from django.core.exceptions import ValidationError
from .models import Author, Tag, Category, Post, Feedback
from django.template.defaultfilters import slugify

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
    
    def clean_name(self):
        name = self.cleanred_data['name']
        name_1 = name.lower()
        if name_1 == "admin" or name__1 == "author":
            raise ValidationError("You might be an author but you can't be the admin")
        return name
    
    def clean_email(self):
        return self.cleaned_data['email'].lower()
    
    def save(self):
        new_author = Author.objects.create(
            name = self.cleaned_data['name'],
            email = self.cleaned_data['email'],
            active = self.cleaned_data['active'],
            created_on = self.cleaned_data['created_on'],
            last_logged_in = self.cleaned_data['last_logged_in'],
        )
        return new_author
    
class TagForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), required=False)
    
    class Meta:
        model = Tag
        fields = '__all__'
        
    def clean_name(self):
        n = self.cleaned_data['name']
        if n.lower() == "tag" or n.lower() == "add" or n.lower() == "update":
            raise ValidationError("Tag name can't be '{}'".format(n))
        return n
        
    def clean_slug(self):
        return self.cleaned_data['slug'].lower()
        
class CategoryForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), required=False)
    
    class Meta:
        model = Category
        fields = '__all__'
        
    def clean_name(self):
        n = self.cleaned_data['name']
        if n.lower() == "tag" or n.lower() == "add" or n.lower() == "update":
            raise ValidationError("Category name can't be '{}".format(n))
        return n
    
    def clean_slug(self):
        return self.cleaned_data['slug'].lower()
    
class PostForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), required=False)
    
    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'category', 'tags',)
        
    def clean_name(self):
        n = self.cleaned_data['title']
        if n.lower() == "post" or n.lower() == "add" or n.lower() == "update":
            raise ValidationError("Post name can't be '{}'".format(n))
        return n
    
    def clean(self):
        cleaned_data = super(PostForm, self).clean() # call parent clean method
        title = cleaned_data.get('title')
        # if title exists create slug using title
        if title:
            cleaned_data['slug'] = slugify(title)
        return cleaned_data
    
class FeedbackForm(forms.ModelForm):
    
    class Meta:
        model = Feedback
        fields = '__all__'