from django.shortcuts import render, redirect, reverse

from customers import models, forms
from genMerch import views as custom_views


class CustomerIndexTemplateView(custom_views.CustomTemplateView):
    template_name = 'customers/customers.html'
    queryset = models.Customer.objects.all()  # pylint: disable=no-member
    default_form = forms.CustomerRegistrationModelForm
    default_context = {'is_customer': True}

    def post(self,request):
        if request.method == 'POST':
            if 'btnUpdate' in request.POST:
                print("update clicked")
                cid = request.POST.get("cid")
                fname = request.POST.get("first_name")
                mname = request.POST.get("middle_name")
                lname = request.POST.get("last_name")
                email = request.POST.get("email")
                pnumber = request.POST.get("phone_number")
                city = request.POST.get("city")
                prov = request.POST.get("province")
                zipc = request.POST.get("zip_code")
                conty = request.POST.get("country")
                bdate = request.POST.get("birthdate")
                gender = request.POST.get("gender")
                stat = request.POST.get("status")
                spouse = request.POST.get("spouse_name")
                spouseOcc = request.POST.get("spouse_occupation")
                children = request.POST.get("number_of_children")
                mother =request.POST.get("mother_name")
                motherOcc = request.POST.get("mother_occupation")
                father = request.POST.get("father_name")
                fatherOCc = request.POST.get("father_occupation")
                height = request.POST.get("height")
                weight = request.POST.get("weight")
                religion = request.POST.get("religion")
                pp = request.FILES["profile_pic"]

                models.Customer.objects.filter(person_ptr_id = cid).update(first_name = fname, middle_name = mname, last_name = lname, profile_pic = pp,   # pylint: disable=no-member
                                city= city, province = prov, zip_code = zipc, country = conty, sex = gender, birthdate=bdate, status=stat,
                                spouse_name = spouse,spouse_occupation = spouseOcc, number_of_children = children, father_name = father,
                                father_occupation = fatherOCc,mother_name = mother, mother_occupation = motherOcc, height=height,weight=weight,
                                religion = religion, email = email, phone_number = pnumber )
                print("customer updated")    
            elif 'btnDelete' in request.POST:
                cid = request.POST.get("cid")
                models.Customer.objects.filter(person_ptr_id = cid).delete() # pylint: disable=no-member
                models.Person.objects.filter(id = cid).delete() # pylint: disable=no-member
                print("customer deleted")
        return redirect('customers:dashboard')

class CustomerRegistrationTemplateView(custom_views.CustomTemplateView):
    template_name = 'customers/customer_reg.html'
    queryset = models.Customer.objects.all()  # pylint: disable=no-member
    default_form = forms.CustomerRegistrationModelForm
    default_context = {'is_customer': True}

    def post(self, request):
        form = self.default_form(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect(reverse('customers:dashboard'))

        context = self.get_context_data()
        context['has_error'] = True

        return render(request, self.template_name, context=context)
