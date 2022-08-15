# Django imports
from django import forms
from django.forms import TextInput, Select, FileInput

# Third-party app imports
from ckeditor.widgets import CKEditorWidget

# Blog app imports
from blog.models.article_models import Article
from blog.models.category_models import Category


class ArticleCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(
                                      approved=True),
                                      empty_label="Select Category",
                                      widget=forms.Select(attrs=
                                                          {
                                                              "class": "form-control selectpicker",
                                                              "type": "text",
                                                              "name": "article-category",
                                                              "id": "articleCategory",
                                                              "data-live-search": "true"
                                                          }
                                      )
                                    )

    class Meta:

        # Article status constants
        DRAFTED = "DRAFTED"
        PUBLISHED = "PUBLISHED"

        # CHOICES
        STATUS_CHOICES = (
            (DRAFTED, 'Draft'),
            (PUBLISHED, 'Publish'),
        )

        model = Article
        fields = ["title", "filelink_one", "filelink_two", "filelink_three", "filelink_four", 'File_hoster_name1', 'File_hoster_name2', 'File_hoster_name3', 'File_hoster_name4', "category", "image", "image_credit", "body", "tags", "status"]
        widgets = {
            'title': TextInput(attrs={
                                     'name': "article-title",
                                     'class': "form-control",
                                     'placeholder': "Enter Article Title",
                                     'id': "articleTitle"
                                     }),

            'filelink_one': TextInput(attrs={
                                        'name': "filelink_one",
                                        'class': "form-control",
                                        'placeholder': "Enter the file link ",
                                        'id': "fileLinkOne"
                                        }),

            'filelink_two': TextInput(attrs={
                                        'name': "filelink_two",
                                        'class': "form-control",
                                        'placeholder': "Enter the file link ",
                                        'id': "fileLinkTwo"
                                        }),

            'filelink_three': TextInput(attrs={
                                        'name': "filelink_three",
                                        'class': "form-control",
                                        'placeholder': "Enter the file link ",
                                        'id': "fileLinkThree"
                                        }),

            'filelink_four': TextInput(attrs={
                                        'name': "filelink_four",
                                        'class': "form-control",
                                        'placeholder': "Enter the file link ",
                                        'id': "fileLinkFour"
                                        }),                                                 


            'File_hoster_name1': TextInput(attrs={
                                        'name': "File_hoster_name1",
                                        'class': "form-control",
                                        'placeholder': "Enter the File hoster name ",
                                        'id': "File_hoster_name1"
                                        }), 

            'File_hoster_name2': TextInput(attrs={
                                        'name': "File_hoster_name2",
                                        'class': "form-control",
                                        'placeholder': "Enter the File hoster name ",
                                        'id': "File_hoster_name2"
                                        }), 

            'File_hoster_name3': TextInput(attrs={
                                        'name': "File_hoster_name3",
                                        'class': "form-control",
                                        'placeholder': "Enter the File hoster name ",
                                        'id': "File_hoster_name3"
                                        }), 


            'File_hoster_name4': TextInput(attrs={
                                        'name': "File_hoster_name4",
                                        'class': "form-control",
                                        'placeholder': "Enter the File hoster name ",
                                        'id': "File_hoster_name4"
                                        }), 


            'image': FileInput(attrs={
                                        "class": "form-control clearablefileinput",
                                        "type": "file",
                                        "id": "articleImage",
                                        "name": "article-image"
                                      }

                               ),

            'image_credit': TextInput(attrs={
                'name': "image_credit",
                'class': "form-control",
                'placeholder': "Example: made4dev.com (Premium Programming T-shirts)",
                'id': "image_credit"
            }),

            'body': forms.CharField(widget=CKEditorWidget(config_name="default", attrs={
                       "rows": 5, "cols": 20,
                       'id': 'content',
                       'name': "article_content",
                       'class': "form-control",
                       })),

            'tags': TextInput(attrs={
                                     'name': "tags",
                                     'class': "form-control",
                                     'placeholder': "Example: sports, game, politics",
                                     'id': "tags",
                                     'data-role': "tagsinput"
                                     }),

            'status': Select(choices=STATUS_CHOICES,
                             attrs=
                             {
                                 "class": "form-control selectpicker",
                                 "name": "status", "type": "text",
                                 "id": "articleStatus",
                                 "data-live-search": "true",
                                 "title": "Select Status"
                             }
                             ),
        }


class ArticleUpdateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(
                                      approved=True),
                                      empty_label="Select Category",
                                      widget=forms.Select(attrs=
                                                          {
                                                              "class": "form-control selectpicker",
                                                              "type": "text",
                                                              "name": "article-category",
                                                              "id": "articleCategory",
                                                              "data-live-search": "true"
                                                          }
                                      )
                                    )

    class Meta:
        # Article status constants
        DRAFTED = "DRAFTED"
        PUBLISHED = "PUBLISHED"

        # CHOICES
        STATUS_CHOICES = (
            (DRAFTED, 'Draft'),
            (PUBLISHED, 'Publish'),
        )

        model = Article
        fields = ["title", "filelink_one", "filelink_two", "filelink_three", "filelink_four", 'File_hoster_name1', 'File_hoster_name2', 'File_hoster_name3', 'File_hoster_name4', "category", "image", "image_credit", "body", "tags", "status"]
        widgets = {
            'title': TextInput(attrs={
                'name': "article-title",
                'class': "form-control",
                'placeholder': "Enter Article Title",
                'id': "articleTitle"
            }),


            'filelink_one': TextInput(attrs={
                                    'name': "filelink_one",
                                    'class': "form-control",
                                    'placeholder': "Enter the file link ",
                                    'id': "fileLinkOne"
                                    }),

             'filelink_two': TextInput(attrs={
                                'name': "filelink_two",
                                'class': "form-control",
                                'placeholder': "Enter the file link ",
                                'id': "fileLinkTwo"
                                }),

            'filelink_three': TextInput(attrs={
                                'name': "filelink_three",
                                'class': "form-control",
                                'placeholder': "Enter the file link ",
                                'id': "fileLinkThree"
                                }),

            'filelink_four': TextInput(attrs={
                                'name': "filelink_four",
                                'class': "form-control",
                                'placeholder': "Enter the file link ",
                                'id': "fileLinkFour"
                                }), 


            'File_hoster_name1': TextInput(attrs={
                                        'name': "File_hoster_name1",
                                        'class': "form-control",
                                        'placeholder': "Enter the File hoster name ",
                                        'id': "File_hoster_name1"
                                        }), 

            'File_hoster_name2': TextInput(attrs={
                                        'name': "File_hoster_name2",
                                        'class': "form-control",
                                        'placeholder': "Enter the File hoster name ",
                                        'id': "File_hoster_name2"
                                        }), 

            'File_hoster_name3': TextInput(attrs={
                                        'name': "File_hoster_name3",
                                        'class': "form-control",
                                        'placeholder': "Enter the File hoster name ",
                                        'id': "File_hoster_name3"
                                        }), 


            'File_hoster_name4': TextInput(attrs={
                                        'name': "File_hoster_name4",
                                        'class': "form-control",
                                        'placeholder': "Enter the File hoster name ",
                                        'id': "File_hoster_name4"
                                        }), 


            'image_credit': TextInput(attrs={
                'name': "image_credit",
                'class': "form-control",
                'placeholder': "Example: made4dev.com (Premium Programming T-shirts)",
                'id': "image_credit"
            }),


            'status': Select(choices=STATUS_CHOICES,
                             attrs=
                             {
                                 "class": "form-control selectpicker",
                                 "name": "status", "type": "text",
                                 "id": "articleStatus",
                                 "data-live-search": "true",
                                 "title": "Select Status"
                             }
                             ),


            'body': forms.CharField(widget=CKEditorWidget(config_name="default", attrs={
                       "rows": 5, "cols": 20,
                       'id': 'content',
                       'name': "article_content",
                       'class': "form-control",
                       })),


            'image': FileInput(attrs={
                "class": "form-control clearablefileinput",
                "type": "file",
                "id": "articleImage",
                "name": "article-image",
            }

            ),

        }
