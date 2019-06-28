from django.shortcuts import render, redirect
from .models import Node, Gateway
from .forms import NodeForm, GatewayForm
from django.contrib.auth.decorators import login_required


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def Home(request):
    if request.user.is_authenticated:
        node_obj = Node.objects.filter(created_by=request.user)
        message = "Nodes Created by: " + str(request.user)
    else:
        node_obj = None
        message = "Hello Visitor!. Looking for records ? If yes, Then Please Sign In. If you don't have an " \
                  "account, you can always Sign Up."
    template_name = 'core/home.html'
    context = {'object': node_obj, 'message': message}
    return render(request, template_name, context)


def GatewayList(request):
    if request.user.is_authenticated:
        gateway_obj = Gateway.objects.filter(created_by=request.user)
        message = "Gateways Created by: " + str(request.user)
    else:
        gateway_obj = None
        message = "You have  to sign in to view this page. If you dont have any account then Sign Up"
    template_name = 'core/gateway_list.html'
    context = {'object': gateway_obj, 'message': message}
    return render(request, template_name, context)


@login_required
def CreateGatewayView(request):
    form = GatewayForm(request.POST or None)
    if form.is_valid():
        f1 = form.save(commit=False)
        f1.created_by = request.user
        f1.save()
        form = GatewayForm()
        return redirect('create-node')
    template_name = 'core/forms-gateway.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required
def CreateNodeView(request):
    form = NodeForm(request.user, request.POST or None )
    if form.is_valid():
        f2 = form.save(commit=False)
        f2.created_by = request.user
        f2.save()
        gateway_object = f2.gateway_id
        gateway_object.number_nodes += 1
        gateway_object.save()
        return redirect('/')
    template_name = 'core/forms-node.html'
    context = {'form': form}
    return render(request, template_name, context)

