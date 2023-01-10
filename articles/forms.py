from django import forms
from .models import Article, Category, ImageArticle, SubCategory, Tag, Condition, Color, MainCategory, Size

# https://forum.djangoproject.com/t/4-way-dependent-chained-dropdown-list-with-django-location-dropdown-list/11526
# https://django-smart-selects.readthedocs.io/en/latest/usage.html#chained-manytomany-selects
# https://moeedrafique.medium.com/how-to-create-dependent-dropdown-in-django-chained-dropdown-82e2b414b501
# https://stackoverflow.com/questions/10558240/django-forms-how-to-create-a-form-with-a-dependent-dropdown
# https://stackoverflow.com/questions/20203806/limit-maximum-choices-of-manytomanyfield
# https://stackoverflow.com/questions/20203806/limit-maximum-choices-of-manytomanyfield
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'main_category', 'description', 'price', 'category', 'subcategory', 'condition', 'color',
                  'size', 'tag', 'photo_main', 'image_article']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'main_category': forms.Select(),
            'description': forms.Textarea(),
            'price': forms.NumberInput(),
            'category': forms.Select(),
            'subcategory': forms.Select(),
            'condition': forms.Select(),
            'color': forms.Select(),
            'size': forms.Select(),
            'tag': forms.SelectMultiple(),
            'photo_main': forms.FileInput(),
            'image_article': forms.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            self.fields['main_category'].widget.attrs.update({
                'class': 'form-select js-choice',
            })
            self.fields['category'].widget.attrs.update({
                'class': 'form-select js-choice',
            })
            self.fields['subcategory'].widget.attrs.update({
                'class': 'form-select js-choice',
            })
            self.fields['condition'].widget.attrs.update({
                'class': 'form-select js-choice',
            })
            self.fields['color'].widget.attrs.update({
                'class': 'form-select js-choice',
            })
            self.fields['size'].widget.attrs.update({
                'class': 'form-select js-choice',
            })

            self.fields['image_article'].widget.attrs.update({
                'multiple': 'true',

            })

