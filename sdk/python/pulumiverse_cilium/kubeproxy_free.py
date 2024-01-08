# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['KubeproxyFreeArgs', 'KubeproxyFree']

@pulumi.input_type
class KubeproxyFreeArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a KubeproxyFree resource.
        :param pulumi.Input[str] name: Name of DaemonSet (Default: `kube-proxy`).
        :param pulumi.Input[str] namespace: Namespace in which to install (Default: `kube-system`).
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of DaemonSet (Default: `kube-proxy`).
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        Namespace in which to install (Default: `kube-system`).
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)


@pulumi.input_type
class _KubeproxyFreeState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering KubeproxyFree resources.
        :param pulumi.Input[str] name: Name of DaemonSet (Default: `kube-proxy`).
        :param pulumi.Input[str] namespace: Namespace in which to install (Default: `kube-system`).
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of DaemonSet (Default: `kube-proxy`).
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        Namespace in which to install (Default: `kube-system`).
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)


class KubeproxyFree(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Disable Kube-Proxy DaemonSet, equivalent to: `kubectl -n kube-system patch daemonset kube-proxy -p '"spec": {"template": {"spec": {"nodeSelector": {"non-existing": "true"}}}}'`.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Name of DaemonSet (Default: `kube-proxy`).
        :param pulumi.Input[str] namespace: Namespace in which to install (Default: `kube-system`).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[KubeproxyFreeArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Disable Kube-Proxy DaemonSet, equivalent to: `kubectl -n kube-system patch daemonset kube-proxy -p '"spec": {"template": {"spec": {"nodeSelector": {"non-existing": "true"}}}}'`.

        :param str resource_name: The name of the resource.
        :param KubeproxyFreeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KubeproxyFreeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KubeproxyFreeArgs.__new__(KubeproxyFreeArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["namespace"] = namespace
        super(KubeproxyFree, __self__).__init__(
            'cilium:index/kubeproxyFree:KubeproxyFree',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            namespace: Optional[pulumi.Input[str]] = None) -> 'KubeproxyFree':
        """
        Get an existing KubeproxyFree resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Name of DaemonSet (Default: `kube-proxy`).
        :param pulumi.Input[str] namespace: Namespace in which to install (Default: `kube-system`).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KubeproxyFreeState.__new__(_KubeproxyFreeState)

        __props__.__dict__["name"] = name
        __props__.__dict__["namespace"] = namespace
        return KubeproxyFree(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of DaemonSet (Default: `kube-proxy`).
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[str]:
        """
        Namespace in which to install (Default: `kube-system`).
        """
        return pulumi.get(self, "namespace")

