# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetClusterStatusResult',
    'AwaitableGetClusterStatusResult',
    'get_cluster_status',
    'get_cluster_status_output',
]

@pulumi.output_type
class GetClusterStatusResult:
    """
    A collection of values returned by getClusterStatus.
    """
    def __init__(__self__, cluster_name=None, exists=None, id=None, instance_groups=None, is_valid=None, needs_update=None):
        if cluster_name and not isinstance(cluster_name, str):
            raise TypeError("Expected argument 'cluster_name' to be a str")
        pulumi.set(__self__, "cluster_name", cluster_name)
        if exists and not isinstance(exists, bool):
            raise TypeError("Expected argument 'exists' to be a bool")
        pulumi.set(__self__, "exists", exists)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_groups and not isinstance(instance_groups, list):
            raise TypeError("Expected argument 'instance_groups' to be a list")
        pulumi.set(__self__, "instance_groups", instance_groups)
        if is_valid and not isinstance(is_valid, bool):
            raise TypeError("Expected argument 'is_valid' to be a bool")
        pulumi.set(__self__, "is_valid", is_valid)
        if needs_update and not isinstance(needs_update, bool):
            raise TypeError("Expected argument 'needs_update' to be a bool")
        pulumi.set(__self__, "needs_update", needs_update)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> str:
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter
    def exists(self) -> bool:
        return pulumi.get(self, "exists")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceGroups")
    def instance_groups(self) -> Sequence[str]:
        return pulumi.get(self, "instance_groups")

    @property
    @pulumi.getter(name="isValid")
    def is_valid(self) -> bool:
        return pulumi.get(self, "is_valid")

    @property
    @pulumi.getter(name="needsUpdate")
    def needs_update(self) -> bool:
        return pulumi.get(self, "needs_update")


class AwaitableGetClusterStatusResult(GetClusterStatusResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterStatusResult(
            cluster_name=self.cluster_name,
            exists=self.exists,
            id=self.id,
            instance_groups=self.instance_groups,
            is_valid=self.is_valid,
            needs_update=self.needs_update)


def get_cluster_status(cluster_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterStatusResult:
    """
    ## # get_cluster_status

    Provides a kOps cluster status data source.

    This data source assumes the cluster has been applied (or updated) see [ClusterUpdater](https://www.terraform.io/docs/resources/cluster_updater).


    :param str cluster_name: - String - ClusterName defines the target cluster name.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('kops:index/getClusterStatus:getClusterStatus', __args__, opts=opts, typ=GetClusterStatusResult).value

    return AwaitableGetClusterStatusResult(
        cluster_name=__ret__.cluster_name,
        exists=__ret__.exists,
        id=__ret__.id,
        instance_groups=__ret__.instance_groups,
        is_valid=__ret__.is_valid,
        needs_update=__ret__.needs_update)


@_utilities.lift_output_func(get_cluster_status)
def get_cluster_status_output(cluster_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterStatusResult]:
    """
    ## # get_cluster_status

    Provides a kOps cluster status data source.

    This data source assumes the cluster has been applied (or updated) see [ClusterUpdater](https://www.terraform.io/docs/resources/cluster_updater).


    :param str cluster_name: - String - ClusterName defines the target cluster name.
    """
    ...
