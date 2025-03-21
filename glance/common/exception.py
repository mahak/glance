# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Glance exception subclasses"""

import urllib.parse as urlparse

from glance.i18n import _

_FATAL_EXCEPTION_FORMAT_ERRORS = False


class RedirectException(Exception):
    def __init__(self, url):
        self.url = urlparse.urlparse(url)


class GlanceException(Exception):
    """
    Base Glance Exception

    To correctly use this class, inherit from it and define
    a 'message' property. That message will get printf'd
    with the keyword arguments provided to the constructor.
    """
    message = _("An unknown exception occurred")

    def __init__(self, message=None, *args, **kwargs):
        if not message:
            message = self.message
        try:
            if kwargs:
                message = message % kwargs
        except Exception:
            if _FATAL_EXCEPTION_FORMAT_ERRORS:
                raise
            else:
                # at least get the core message out if something happened
                pass
        self.msg = message
        super(GlanceException, self).__init__(message)


class MissingCredentialError(GlanceException):
    message = _("Missing required credential: %(required)s")


class BadAuthStrategy(GlanceException):
    message = _("Incorrect auth strategy, expected \"%(expected)s\" but "
                "received \"%(received)s\"")


class NotFound(GlanceException):
    message = _("An object with the specified identifier was not found.")


class BadStoreUri(GlanceException):
    message = _("The Store URI was malformed.")


class Duplicate(GlanceException):
    message = _("An object with the same identifier already exists.")


class Conflict(GlanceException):
    message = _("An object with the same identifier is currently being "
                "operated on.")


class StorageQuotaFull(GlanceException):
    message = _("The size of the data %(image_size)s will exceed the limit. "
                "%(remaining)s bytes remaining.")


class AuthBadRequest(GlanceException):
    message = _("Connect error/bad request to Auth service at URL %(url)s.")


class AuthUrlNotFound(GlanceException):
    message = _("Auth service at URL %(url)s not found.")


class AuthorizationFailure(GlanceException):
    message = _("Authorization failed.")


class NotAuthenticated(GlanceException):
    message = _("You are not authenticated.")


class UploadException(GlanceException):
    message = _('Image upload problem: %s')


class Forbidden(GlanceException):
    message = _("You are not authorized to complete %(action)s action.")


class ForbiddenPublicImage(Forbidden):
    message = _("You are not authorized to complete this action.")


class ProtectedImageDelete(Forbidden):
    message = _("Image %(image_id)s is protected and cannot be deleted.")


class ProtectedMetadefNamespaceDelete(Forbidden):
    message = _("Metadata definition namespace %(namespace)s is protected"
                " and cannot be deleted.")


class ProtectedMetadefNamespacePropDelete(Forbidden):
    message = _("Metadata definition property %(property_name)s is protected"
                " and cannot be deleted.")


class ProtectedMetadefObjectDelete(Forbidden):
    message = _("Metadata definition object %(object_name)s is protected"
                " and cannot be deleted.")


class ProtectedMetadefResourceTypeAssociationDelete(Forbidden):
    message = _("Metadata definition resource-type-association"
                " %(resource_type)s is protected and cannot be deleted.")


class ProtectedMetadefResourceTypeSystemDelete(Forbidden):
    message = _("Metadata definition resource-type %(resource_type_name)s is"
                " a seeded-system type and cannot be deleted.")


class ProtectedMetadefTagDelete(Forbidden):
    message = _("Metadata definition tag %(tag_name)s is protected"
                " and cannot be deleted.")


class Invalid(GlanceException):
    message = _("Data supplied was not valid.")


class InvalidSortKey(Invalid):
    message = _("Sort key supplied was not valid.")


class InvalidSortDir(Invalid):
    message = _("Sort direction supplied was not valid.")


class InvalidPropertyProtectionConfiguration(Invalid):
    message = _("Invalid configuration in property protection file.")


class InvalidSwiftStoreConfiguration(Invalid):
    message = _("Invalid configuration in glance-swift conf file.")


class InvalidFilterOperatorValue(Invalid):
    message = _("Unable to filter using the specified operator.")


class InvalidFilterRangeValue(Invalid):
    message = _("Unable to filter using the specified range.")


class InvalidOptionValue(Invalid):
    message = _("Invalid value for option %(option)s: %(value)s")


class ReadonlyProperty(Forbidden):
    message = _("Attribute '%(property)s' is read-only.")


class ReservedProperty(Forbidden):
    message = _("Attribute '%(property)s' is reserved.")


class AuthorizationRedirect(GlanceException):
    message = _("Redirecting to %(uri)s for authorization.")


class ClientConnectionError(GlanceException):
    message = _("There was an error connecting to a server")


class ClientConfigurationError(GlanceException):
    message = _("There was an error configuring the client.")


class MultipleChoices(GlanceException):
    message = _("The request returned a 302 Multiple Choices. This generally "
                "means that you have not included a version indicator in a "
                "request URI.\n\nThe body of response returned:\n%(body)s")


class LimitExceeded(GlanceException):
    message = _("The request returned a 413 Request Entity Too Large. This "
                "generally means that rate limiting or a quota threshold was "
                "breached.\n\nThe response body:\n%(body)s")

    def __init__(self, *args, **kwargs):
        self.retry_after = (int(kwargs['retry']) if kwargs.get('retry')
                            else None)
        super(LimitExceeded, self).__init__(*args, **kwargs)


class ServiceUnavailable(GlanceException):
    message = _("The request returned 503 Service Unavailable. This "
                "generally occurs on service overload or other transient "
                "outage.")

    def __init__(self, *args, **kwargs):
        self.retry_after = (int(kwargs['retry']) if kwargs.get('retry')
                            else None)
        super(ServiceUnavailable, self).__init__(*args, **kwargs)


class ServerError(GlanceException):
    message = _("The request returned 500 Internal Server Error.")


class UnexpectedStatus(GlanceException):
    message = _("The request returned an unexpected status: %(status)s."
                "\n\nThe response body:\n%(body)s")


class InvalidContentType(GlanceException):
    message = _("Invalid content type %(content_type)s")


class BadRegistryConnectionConfiguration(GlanceException):
    message = _("Registry was not configured correctly on API server. "
                "Reason: %(reason)s")


class BadDriverConfiguration(GlanceException):
    message = _("Driver %(driver_name)s could not be configured correctly. "
                "Reason: %(reason)s")


class MaxRedirectsExceeded(GlanceException):
    message = _("Maximum redirects (%(redirects)s) was exceeded.")


class InvalidRedirect(GlanceException):
    message = _("Received invalid HTTP redirect.")


class NoServiceEndpoint(GlanceException):
    message = _("Response from Keystone does not contain a Glance endpoint.")


class RegionAmbiguity(GlanceException):
    message = _("Multiple 'image' service matches for region %(region)s. This "
                "generally means that a region is required and you have not "
                "supplied one.")


class WorkerCreationFailure(GlanceException):
    message = _("Server worker creation failed: %(reason)s.")


class SchemaLoadError(GlanceException):
    message = _("Unable to load schema: %(reason)s")


class InvalidObject(GlanceException):
    message = _("Provided object does not match schema "
                "'%(schema)s': %(reason)s")


class ImageSizeLimitExceeded(GlanceException):
    message = _("The provided image is too large.")


class FailedToGetScrubberJobs(GlanceException):
    message = _("Scrubber encountered an error while trying to fetch "
                "scrub jobs.")


class ImageMemberLimitExceeded(LimitExceeded):
    message = _("The limit has been exceeded on the number of allowed image "
                "members for this image. Attempted: %(attempted)s, "
                "Maximum: %(maximum)s")


class ImagePropertyLimitExceeded(LimitExceeded):
    message = _("The limit has been exceeded on the number of allowed image "
                "properties. Attempted: %(attempted)s, Maximum: %(maximum)s")


class ImageTagLimitExceeded(LimitExceeded):
    message = _("The limit has been exceeded on the number of allowed image "
                "tags. Attempted: %(attempted)s, Maximum: %(maximum)s")


class ImageLocationLimitExceeded(LimitExceeded):
    message = _("The limit has been exceeded on the number of allowed image "
                "locations. Attempted: %(attempted)s, Maximum: %(maximum)s")


class SIGHUPInterrupt(GlanceException):
    message = _("System SIGHUP signal received.")


class RPCError(GlanceException):
    message = _("%(cls)s exception was raised in the last rpc call: %(val)s")


class TaskException(GlanceException):
    message = _("An unknown task exception occurred")


class BadTaskConfiguration(GlanceException):
    message = _("Task was not configured properly")


class ImageNotFound(NotFound):
    message = _("Image with the given id %(image_id)s was not found")


class TaskNotFound(TaskException, NotFound):
    message = _("Task with the given id %(task_id)s was not found")


class InvalidTaskStatus(TaskException, Invalid):
    message = _("Provided status of task is unsupported: %(status)s")


class InvalidTaskType(TaskException, Invalid):
    message = _("Provided type of task is unsupported: %(type)s")


class InvalidTaskStatusTransition(TaskException, Invalid):
    message = _("Status transition from %(cur_status)s to"
                " %(new_status)s is not allowed")


class ImportTaskError(TaskException, Invalid):
    message = _("An import task exception occurred")


class TaskAbortedError(ImportTaskError):
    message = _("Task was aborted externally")


class DuplicateLocation(Duplicate):
    message = _("The location %(location)s already exists")


class InvalidParameterValue(Invalid):
    message = _("Invalid value '%(value)s' for parameter '%(param)s': "
                "%(extra_msg)s")


class InvalidImageStatusTransition(Invalid):
    message = _("Image status transition from %(cur_status)s to"
                " %(new_status)s is not allowed")


class MetadefDuplicateNamespace(Duplicate):
    message = _("The metadata definition namespace=%(namespace_name)s"
                " already exists.")


class MetadefDuplicateObject(Duplicate):
    message = _("A metadata definition object with name=%(object_name)s"
                " already exists in namespace=%(namespace_name)s.")


class MetadefDuplicateProperty(Duplicate):
    message = _("A metadata definition property with name=%(property_name)s"
                " already exists in namespace=%(namespace_name)s.")


class MetadefDuplicateResourceType(Duplicate):
    message = _("A metadata definition resource-type with"
                " name=%(resource_type_name)s already exists.")


class MetadefDuplicateResourceTypeAssociation(Duplicate):
    message = _("The metadata definition resource-type association of"
                " resource-type=%(resource_type_name)s to"
                " namespace=%(namespace_name)s"
                " already exists.")


class MetadefDuplicateTag(Duplicate):
    message = _("A metadata tag with name=%(name)s"
                " already exists in namespace=%(namespace_name)s."
                " (Please note that metadata tag names are"
                " case insensitive).")


class MetadefForbidden(Forbidden):
    message = _("You are not authorized to complete this action.")


class MetadefIntegrityError(Forbidden):
    message = _("The metadata definition %(record_type)s with"
                " name=%(record_name)s not deleted."
                " Other records still refer to it.")


class MetadefNamespaceNotFound(NotFound):
    message = _("Metadata definition namespace=%(namespace_name)s"
                " was not found.")


class MetadefObjectNotFound(NotFound):
    message = _("The metadata definition object with"
                " name=%(object_name)s was not found in"
                " namespace=%(namespace_name)s.")


class MetadefPropertyNotFound(NotFound):
    message = _("The metadata definition property with"
                " name=%(property_name)s was not found in"
                " namespace=%(namespace_name)s.")


class MetadefResourceTypeNotFound(NotFound):
    message = _("The metadata definition resource-type with"
                " name=%(resource_type_name)s, was not found.")


class MetadefResourceTypeAssociationNotFound(NotFound):
    message = _("The metadata definition resource-type association of"
                " resource-type=%(resource_type_name)s to"
                " namespace=%(namespace_name)s,"
                " was not found.")


class MetadefTagNotFound(NotFound):
    message = _("The metadata definition tag with"
                " name=%(name)s was not found in"
                " namespace=%(namespace_name)s.")


class InvalidDataMigrationScript(GlanceException):
    message = _("Invalid data migration script '%(script)s'. A valid data "
                "migration script must implement functions 'has_migrations' "
                "and 'migrate'.")


class GlanceEndpointNotFound(NotFound):
    message = _("%(interface)s glance endpoint not "
                "found for region %(region)s")


class InvalidImageData(Invalid):
    message = _("Image data is not acceptable or does not match parameters")
