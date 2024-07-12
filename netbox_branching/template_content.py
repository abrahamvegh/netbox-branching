from django.contrib.contenttypes.models import ContentType
from netbox.plugins import PluginTemplateExtension

from .choices import BranchStatusChoices
from .contextvars import active_branch
from .models import Branch, ChangeDiff

__all__ = (
    'BranchNotification',
    'BranchSelector',
    'template_extensions',
)


class BranchSelector(PluginTemplateExtension):

    def navbar(self):
        return self.render('netbox_branching/inc/branch_selector.html', extra_context={
            'active_branch': active_branch.get(),
            'branches': Branch.objects.exclude(status=BranchStatusChoices.MERGED),
        })


class BranchNotification(PluginTemplateExtension):

    def alerts(self):
        instance = self.context['object']
        ct = ContentType.objects.get_for_model(instance)
        branches = [
            diff.branch for diff in ChangeDiff.objects.filter(object_type=ct, object_id=instance.pk).only('branch')
        ]
        return self.render('netbox_branching/inc/modified_notice.html', extra_context={
            'branches': branches,
        })


template_extensions = [BranchSelector, BranchNotification]
