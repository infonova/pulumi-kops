# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'Aws',
    'AwsAssumeRole',
    'Klog',
    'KlogVerbosity',
    'Openstack',
]

@pulumi.output_type
class Aws(dict):
    def __init__(__self__, *,
                 access_key: Optional[str] = None,
                 assume_role: Optional['outputs.AwsAssumeRole'] = None,
                 profile: Optional[str] = None,
                 region: Optional[str] = None,
                 s3_access_key: Optional[str] = None,
                 s3_endpoint: Optional[str] = None,
                 s3_region: Optional[str] = None,
                 s3_secret_key: Optional[str] = None,
                 secret_key: Optional[str] = None,
                 skip_region_check: Optional[bool] = None):
        if access_key is not None:
            pulumi.set(__self__, "access_key", access_key)
        if assume_role is not None:
            pulumi.set(__self__, "assume_role", assume_role)
        if profile is not None:
            pulumi.set(__self__, "profile", profile)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if s3_access_key is not None:
            pulumi.set(__self__, "s3_access_key", s3_access_key)
        if s3_endpoint is not None:
            pulumi.set(__self__, "s3_endpoint", s3_endpoint)
        if s3_region is not None:
            pulumi.set(__self__, "s3_region", s3_region)
        if s3_secret_key is not None:
            pulumi.set(__self__, "s3_secret_key", s3_secret_key)
        if secret_key is not None:
            pulumi.set(__self__, "secret_key", secret_key)
        if skip_region_check is not None:
            pulumi.set(__self__, "skip_region_check", skip_region_check)

    @property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> Optional[str]:
        return pulumi.get(self, "access_key")

    @property
    @pulumi.getter(name="assumeRole")
    def assume_role(self) -> Optional['outputs.AwsAssumeRole']:
        return pulumi.get(self, "assume_role")

    @property
    @pulumi.getter
    def profile(self) -> Optional[str]:
        return pulumi.get(self, "profile")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="s3AccessKey")
    def s3_access_key(self) -> Optional[str]:
        return pulumi.get(self, "s3_access_key")

    @property
    @pulumi.getter(name="s3Endpoint")
    def s3_endpoint(self) -> Optional[str]:
        return pulumi.get(self, "s3_endpoint")

    @property
    @pulumi.getter(name="s3Region")
    def s3_region(self) -> Optional[str]:
        return pulumi.get(self, "s3_region")

    @property
    @pulumi.getter(name="s3SecretKey")
    def s3_secret_key(self) -> Optional[str]:
        return pulumi.get(self, "s3_secret_key")

    @property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> Optional[str]:
        return pulumi.get(self, "secret_key")

    @property
    @pulumi.getter(name="skipRegionCheck")
    def skip_region_check(self) -> Optional[bool]:
        return pulumi.get(self, "skip_region_check")


@pulumi.output_type
class AwsAssumeRole(dict):
    def __init__(__self__, *,
                 role_arn: Optional[str] = None):
        if role_arn is not None:
            pulumi.set(__self__, "role_arn", role_arn)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[str]:
        return pulumi.get(self, "role_arn")


@pulumi.output_type
class Klog(dict):
    def __init__(__self__, *,
                 verbosity: Optional['outputs.KlogVerbosity'] = None):
        if verbosity is not None:
            pulumi.set(__self__, "verbosity", verbosity)

    @property
    @pulumi.getter
    def verbosity(self) -> Optional['outputs.KlogVerbosity']:
        return pulumi.get(self, "verbosity")


@pulumi.output_type
class KlogVerbosity(dict):
    def __init__(__self__, *,
                 value: Optional[int] = None):
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[int]:
        return pulumi.get(self, "value")


@pulumi.output_type
class Openstack(dict):
    def __init__(__self__, *,
                 application_credential_id: Optional[str] = None,
                 application_credential_secret: Optional[str] = None,
                 auth_url: Optional[str] = None,
                 domain_id: Optional[str] = None,
                 domain_name: Optional[str] = None,
                 password: Optional[str] = None,
                 project_domain_id: Optional[str] = None,
                 project_domain_name: Optional[str] = None,
                 project_id: Optional[str] = None,
                 project_name: Optional[str] = None,
                 region_name: Optional[str] = None,
                 tenant_id: Optional[str] = None,
                 tenant_name: Optional[str] = None,
                 username: Optional[str] = None):
        if application_credential_id is not None:
            pulumi.set(__self__, "application_credential_id", application_credential_id)
        if application_credential_secret is not None:
            pulumi.set(__self__, "application_credential_secret", application_credential_secret)
        if auth_url is not None:
            pulumi.set(__self__, "auth_url", auth_url)
        if domain_id is not None:
            pulumi.set(__self__, "domain_id", domain_id)
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if project_domain_id is not None:
            pulumi.set(__self__, "project_domain_id", project_domain_id)
        if project_domain_name is not None:
            pulumi.set(__self__, "project_domain_name", project_domain_name)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if project_name is not None:
            pulumi.set(__self__, "project_name", project_name)
        if region_name is not None:
            pulumi.set(__self__, "region_name", region_name)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)
        if tenant_name is not None:
            pulumi.set(__self__, "tenant_name", tenant_name)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="applicationCredentialId")
    def application_credential_id(self) -> Optional[str]:
        return pulumi.get(self, "application_credential_id")

    @property
    @pulumi.getter(name="applicationCredentialSecret")
    def application_credential_secret(self) -> Optional[str]:
        return pulumi.get(self, "application_credential_secret")

    @property
    @pulumi.getter(name="authUrl")
    def auth_url(self) -> Optional[str]:
        return pulumi.get(self, "auth_url")

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[str]:
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[str]:
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter
    def password(self) -> Optional[str]:
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="projectDomainId")
    def project_domain_id(self) -> Optional[str]:
        return pulumi.get(self, "project_domain_id")

    @property
    @pulumi.getter(name="projectDomainName")
    def project_domain_name(self) -> Optional[str]:
        return pulumi.get(self, "project_domain_name")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[str]:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> Optional[str]:
        return pulumi.get(self, "project_name")

    @property
    @pulumi.getter(name="regionName")
    def region_name(self) -> Optional[str]:
        return pulumi.get(self, "region_name")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="tenantName")
    def tenant_name(self) -> Optional[str]:
        return pulumi.get(self, "tenant_name")

    @property
    @pulumi.getter
    def username(self) -> Optional[str]:
        return pulumi.get(self, "username")

