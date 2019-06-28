from django import forms
from .models import Node, Gateway


class GatewayForm(forms.ModelForm):
    class Meta:
        model = Gateway
        exclude = ['created_by', 'number_nodes']


class NodeForm(forms.ModelForm):
    class Meta:
        model = Node
        exclude = ['created_by']

    def __init__(self, user, *args, **kwargs):
        super(NodeForm, self).__init__(*args, **kwargs)
        self.fields['gateway_id'].queryset = Gateway.objects.filter(created_by=user)
