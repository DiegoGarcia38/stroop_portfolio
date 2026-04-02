from multiprocessing import context

from django.shortcuts import render
from math import ceil
from django.contrib import messages
from .models import (
		UserProfile,
		Blog,
		Portfolio,
		Testimonial,
		Certificate,
		WorkExperience
	)

from django.views import generic


from . forms import ContactForm


class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		profile = UserProfile.objects.first()
		testimonials = Testimonial.objects.filter(is_active=True)
		certificates = Certificate.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)
		work_experience = WorkExperience.objects.order_by('-start_date')
		skills = list(profile.skills.filter(is_key_skill=False))
		col1 = skills[::2]
		col2 = skills[1::2]
		context["profile"] = profile
		context["col1"] = col1
		context["col2"] = col2
		context["testimonials"] = testimonials
		context["work_experience"] = work_experience
		context["certificates"] = certificates
		context["blogs"] = blogs
		context["portfolio"] = portfolio
		return context


class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Gracias! Estaremos en contacto contigo pronto/Thank you. We will be in touch soon.')
		return super().form_valid(form)


class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "main/portfolio.html"

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "main/portfolio-detail.html"

class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"
