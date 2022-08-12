from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView,TemplateView

from .models import Review

# Create your views here.

class Best_practices(TemplateView):
    template_name = 'docs/best_practices.html'


class How_it_all_works(TemplateView):
    template_name = 'docs/how_it_all_works.html'


class How_to_guides(TemplateView):
    template_name = 'docs/how_to_guides.html'


class Introduction(TemplateView):
    template_name = 'docs/introduction.html'


class Technical_reference(TemplateView):
    template_name = 'docs/technical_reference.html'


class Tutorials(TemplateView):
    template_name = 'docs/tutorials.html'

#form here !!!!
class Rate_us(ListView):
    model = Review
    template_name = 'docs/rate_us.html'
    context_object_name = 'review'

# since it has a form which returns the method post lets redefine that method
    def post(self, request):
        if request.method == 'POST':
            # getting the data
            m = Review()
            m.name = request.POST.get('name')
            m.role = request.POST.get('role')
            m.body = request.POST.get('comment')
            m.save()
            # so it still shows what it was given previously
            vi = get_list_or_404(Review)
        return render(request, 'docs/rate_us.html',
        {'review':vi }
        )

