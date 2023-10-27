"""
Use the `AdminTask` object to run administrative commands with the `wsadmin` tool.

The set of available administrative commands is discovered dynamically when the scripting 
client is started and **depends on the edition** of WebSphere Application Server you install.

For more info see the [official documentation](https://www.ibm.com/docs/en/was-nd/8.5.5?topic=scripting-commands-admintask-object-using-wsadmin).

!!! Note
    All methods and descriptions were generated using the `AdminTask.help("-commands")` command.
"""

from typing import Any as _Any, Literal as _Literal, Union as _Union, overload as _overload, List as _List

from wsadmin_type_hints.typing_objects.object_name import ConfigurationObjectName
from wsadmin_type_hints.typing_objects.wsadmin_types import MultilineList


def WIMCheckPassword(*args: _Any) -> _Any:
	""" Validates the user/pasword in the Federated repositories user registry """
	...

def activateEdition(*args: _Any) -> _Any:
	""" Marks the state of an edition as ACTIVE. """
	...

def addActionToRule(*args: _Any) -> _Any:
	""" Use this command to add an action to a rule. """
	...

def addAdminIdToUserRegObj(*args: _Any) -> _Any:
	""" Adds the adminId to the user registry object in the security.xml file """
	...

def addCompUnit(*args: _Any) -> _Any:
	""" Add a composition unit, based on an asset or another business-level application, to a business-level application. """
	...

def addConditionalTraceRuleForIntelligentManagement(*args: _Any) -> _Any:
	""" Add conditional trace for Intelligent Management """
	...

def addDefaultAction(*args: _Any) -> _Any:
	""" Use this command to add a default action to a ruleset. """
	...

def addDisabledSessionCookie(*args: _Any) -> _Any:
	""" Adds a cookie configuration that applications will not be able to programmatically modify """
	...

def addExternalBundleRepository(*args: _Any) -> _Any:
	""" Adds an external bundle repository to the configuration.  Requires a repository name and a URL. """
	...

def addFeaturesToServer(*args: _Any) -> _Any:
	""" Add feature pack or stack product features to existing server """
	...

def addFileRegistryAccount(*args: _Any) -> _Any:
	""" Adds an account to the file registry. """
	...

def addForeignServersToDynamicCluster(*args: _Any) -> _Any:
	""" Add foreign servers to dynamic cluster """
	...

def addGroupToBusConnectorRole(*args: _Any) -> _Any:
	""" Give a group permission to connect to the bus specified. """
	...

def addGroupToDefaultRole(*args: _Any) -> _Any:
	""" Grants a group default access to all local destinations on the bus for the specified role. """
	...

def addGroupToDestinationRole(*args: _Any) -> _Any:
	""" Grants a group access to a destination for the specified destination role. """
	...

def addGroupToForeignBusRole(*args: _Any) -> _Any:
	""" Grants a group access to a foreign bus from the local bus specified for the specified destination role. """
	...

def addGroupToTopicRole(*args: _Any) -> _Any:
	""" Gives a group permission to access the topic for the specified role. """
	...

def addGroupToTopicSpaceRootRole(*args: _Any) -> _Any:
	""" Gives a group permission to access the topic space for the specified role. """
	...

def addIdMgrLDAPAttr(*args: _Any) -> _Any:
	""" Adds an LDAP attribute configuration to the LDAP repository configuration. """
	...

def addIdMgrLDAPAttrNotSupported(*args: _Any) -> _Any:
	""" Adds a configuration for a virtual member manager property not supported by a specific LDAP repository. """
	...

def addIdMgrLDAPBackupServer(*args: _Any) -> _Any:
	""" Sets up a backup LDAP server. """
	...

def addIdMgrLDAPEntityType(*args: _Any) -> _Any:
	""" Adds an LDAP entity type definition to the LDAP repository configuration. """
	...

def addIdMgrLDAPEntityTypeRDNAttr(*args: _Any) -> _Any:
	""" Adds RDN attribute configuration to an LDAP entity type configuration. """
	...

def addIdMgrLDAPExternalIdAttr(*args: _Any) -> _Any:
	""" Adds a configuration for an LDAP attribute used as an external ID. """
	...

def addIdMgrLDAPGroupDynamicMemberAttr(*args: _Any) -> _Any:
	""" Adds a dynamic member attribute configuration to an LDAP group configuration. """
	...

def addIdMgrLDAPGroupMemberAttr(*args: _Any) -> _Any:
	""" Adds a member attribute configuration to the LDAP group configuration. """
	...

def addIdMgrLDAPServer(*args: _Any) -> _Any:
	""" Adds an LDAP server to the LDAP repository configuration. """
	...

def addIdMgrPropertyToEntityTypes(*args: _Any) -> _Any:
	""" Adds a property to one or more entity types either into repositories or into the property extension repository. """
	...

def addIdMgrRealmBaseEntry(*args: _Any) -> _Any:
	""" Adds a base entry to a specified realm configuration. """
	...

def addIdMgrRepositoryBaseEntry(*args: _Any) -> _Any:
	""" Adds a base entry to the specified repository. """
	...

def addLocalRepositoryBundle(*args: _Any) -> _Any:
	""" Adds a bundle to the internal bundle repository. """
	...

def addMemberToGroup(*args: _Any) -> _Any:
	""" Adds a member (user or group) to a group. """
	...

def addMemberToManagedNodeGroup(*args: _Any) -> _Any:
	""" This command is used to add members to a group of managed nodes. (deprecated) """
	...

def addMemberToTargetGroup(*args: _Any) -> _Any:
	""" This command is used to add members to a target group. """
	...

def addMiddlewareAppWebModule(*args: _Any) -> _Any:
	""" Use this command to add a web module to a middleware application. """
	...

def addMiddlewareTarget(*args: _Any) -> _Any:
	""" Use this command to add a deployment target to a middleware application. """
	...

def addNodeGroupMember(*args: _Any) -> _Any:
	""" add node to the node group """
	...

def addOSGiExtension(*args: _Any) -> _Any:
	""" Adds an extension to the composition unit. """
	...

def addOSGiExtensions(*args: _Any) -> _Any:
	""" Adds multiple extensions to the composition unit. """
	...

def addPluginPropertyForIntelligentManagement(*args: _Any) -> _Any:
	""" Add plug-in property for Intelligent Management """
	...

def addPolicyType(*args: _Any) -> _Any:
	""" The addPolicyType command creates a policy type with default values for the specified policy set. You may indicate whether to enable or disable the added policy type. """
	...

def addProductInfo(*args: _Any) -> _Any:
	""" Add feature pack or stack product information to product info. """
	...

def addRemoteCellToIntelligentManagement(*args: _Any) -> _Any:
	""" Command to add remote cell connectors to Intelligent Management """
	...

def addResourceToAuthorizationGroup(*args: _Any) -> _Any:
	""" Add resources to an existing authorization group. """
	...

def addRoutingPolicyRoutingRule(*args: _Any) -> _Any:
	""" Use this command to add a routing rule to an existing workclass """
	...

def addRoutingRule(*args: _Any) -> _Any:
	""" Use this command to add a routing policy rule. """
	...

def addRuleToRuleset(*args: _Any) -> _Any:
	""" Use this command to add a rule to a ruleset. """
	...

def addSAMLTAISSO(*args: _Any) -> _Any:
	""" This command adds the SAML Single Sign-On (SSO) service provider (SP) to the security configuration SAML TAI. """
	...

def addSIBBootstrapMember(*args: _Any) -> _Any:
	""" Nominates a server or cluster for use as a bootstrap server. """
	...

def addSIBPermittedChain(*args: _Any) -> _Any:
	""" Adds the specified chain to the list of permitted chains for the specified bus. """
	...

def addSIBWSInboundPort(*args: _Any) -> _Any:
	""" Add an inbound port to an inbound service. """
	...

def addSIBWSOutboundPort(*args: _Any) -> _Any:
	""" Add an outbound port to an outbound service. """
	...

def addSIBusMember(*args: _Any) -> _Any:
	""" Add a member to a bus. """
	...

def addSTSProperty(*args: _Any) -> _Any:
	""" Add a configuration property under a configuration group. """
	...

def addServicePolicyRoutingRule(*args: _Any) -> _Any:
	""" Use this command to add a routing rule to an existing workclass """
	...

def addServiceRule(*args: _Any) -> _Any:
	""" Use this command to add a service policy rule. """
	...

def addSignerCertificate(*args: _Any) -> _Any:
	""" Add a signer certificates from a certificate file to a keystore. """
	...

def addSpnegoFilter(*args: _Any) -> _Any:
	""" This command adds SPNEGO Web authentication filter in the security configuration. """
	...

def addSpnegoTAIProperties(*args: _Any) -> _Any:
	""" This command adds SPNEGO TAI properties in the security configuration. """
	...

def addToAdminAuthz(*args: _Any) -> _Any:
	""" Adds the input administrative user to admin-authz.xml. """
	...

def addToPolicySetAttachment(*args: _Any) -> _Any:
	""" The addToPolicySetAttachment command adds additional resources that apply to a policy set attachment. """
	...

def addTrustedRealms(*args: _Any) -> _Any:
	""" Adds a realm or list of realms to the list of trusted realms in a security domain or in global security. """
	...

def addUserToBusConnectorRole(*args: _Any) -> _Any:
	""" Give a user permission to connect to the bus specified. """
	...

def addUserToDefaultRole(*args: _Any) -> _Any:
	""" Grants a user default access to all local destinations on the bus for the specified role. """
	...

def addUserToDestinationRole(*args: _Any) -> _Any:
	""" Grants a user access to a destination for the specified destination role. """
	...

def addUserToForeignBusRole(*args: _Any) -> _Any:
	""" Grants a user access to a foreign bus from the local bus specified for the specified destination role. """
	...

def addUserToTopicRole(*args: _Any) -> _Any:
	""" Gives a user permission to access the topic for the specified role. """
	...

def addUserToTopicSpaceRootRole(*args: _Any) -> _Any:
	""" Gives a user permission to access the topic space for the specified role. """
	...

def addWSGWTargetService(*args: _Any) -> _Any:
	""" addWSGWTargetService.description """
	...

def addWebServerRoutingRule(*args: _Any) -> _Any:
	""" Use this command to create a new routing rule. """
	...

def applyConfigProperties(*args: _Any) -> _Any:
	""" Apply configuration as specified in properties file """
	...

def applyProfileSecuritySettings(*args: _Any) -> _Any:
	""" Applies the security settings selected during install or profile creation time. """
	...

def applyWizardSettings(*args: _Any) -> _Any:
	""" Applies current Security Wizard settings from the workspace. """
	...

def assignSTSEndpointTokenType(*args: _Any) -> _Any:
	""" Assign a token type to be issued for the client to access a given endpoint. Endpoints must be unique. If the local name parameter is omitted, the default token type is assumed. """
	...

def attachServiceMap(*args: _Any) -> _Any:
	""" Use the "attachServiceMap" command to attach a service map to a local mapping service. """
	...

def autogenLTPA(*args: _Any) -> _Any:
	""" Auto-generates an LTPA password and updates the LTPA object in the security.xml. """
	...

def autogenServerId(*args: _Any) -> _Any:
	""" Auto-generates a server Id and updates the internalServerId field in the security.xml. """
	...

def backupJobManager(*args: _Any) -> _Any:
	""" Backs up the job manager database to a specified location. """
	...

def binaryAuditLogReader(*args: _Any) -> _Any:
	""" Binary Audit Log Reader Command """
	...

def canNodeJoinNodeGroup(*args: _Any) -> _Any:
	""" Check if a specified node can be added to a specified node group. """
	...

def cancelValidation(*args: _Any) -> _Any:
	""" Cancels the validation mode of an edition. """
	...

def changeClusterShortName(*args: _Any) -> _Any:
	""" A command that can be used to change the cluster's short name. """
	...

def changeFileRegistryAccountPassword(*args: _Any) -> _Any:
	""" Change the password of an account in the file registry. """
	...

def changeHostName(*args: _Any) -> _Any:
	""" Change the host name of a node """
	...

def changeKeyStorePassword(*args: _Any) -> _Any:
	""" Change the password of a keystore. This will automatically save the new password to the configuration. """
	...

def changeMultipleKeyStorePasswords(*args: _Any) -> _Any:
	""" Change all the passwords for the keystores that use the password provided, which automatically saves the new passwords to the configuration. """
	...

def changeMyPassword(*args: _Any) -> _Any:
	""" Changes the password of this logged-in user. """
	...

def changeRoutingDefaultRulesAction(*args: _Any) -> _Any:
	""" Use this command to change a rules routing policy default action. """
	...

def changeRoutingRuleAction(*args: _Any) -> _Any:
	""" Use this command to change a routing policy action for a rule. """
	...

def changeRoutingRuleExpression(*args: _Any) -> _Any:
	""" Use this command to change a routing policy rule expression. """
	...

def changeRoutingRulePriority(*args: _Any) -> _Any:
	""" Use this command to change a routing policy rule priority. """
	...

def changeRuleExpression(*args: _Any) -> _Any:
	""" Use this command to change a rule expression. """
	...

def changeRulePriority(*args: _Any) -> _Any:
	""" Use this command to change a rule prioritiy. """
	...

def changeServerGenericShortName(*args: _Any) -> _Any:
	""" A command that can be used to change the server generic short name. """
	...

def changeServerSpecificShortName(*args: _Any) -> _Any:
	""" A command that can be used to change the server specific short name. """
	...

def changeServiceDefaultRulesAction(*args: _Any) -> _Any:
	""" Use this command to change a rules service policy default action. """
	...

def changeServiceRuleAction(*args: _Any) -> _Any:
	""" Use this command to change a service policy action for a rule. """
	...

def changeServiceRuleExpression(*args: _Any) -> _Any:
	""" Use this command to change a service policy rule expression. """
	...

def changeServiceRulePriority(*args: _Any) -> _Any:
	""" Use this command to change a service policy rule priority. """
	...

def changeWebServerRoutingRuleAction(*args: _Any) -> _Any:
	""" Use this command to change the action associated with an existing routing rule. """
	...

def changeWebServerRoutingRuleExpression(*args: _Any) -> _Any:
	""" Use this command to change the expression associated with an existing routing rule. """
	...

def changeWebServerRoutingRuleOrder(*args: _Any) -> _Any:
	""" Use this command to change the order associated with an existing routing rule. """
	...

def checkDynamicClustersForNodeGroupRemoval(*args: _Any) -> _Any:
	""" Check Node Group for XD Dynamic Clusters """
	...

def checkMode(*args: _Any) -> _Any:
	""" checks the maintenance mode indicator on specified server """
	...

def checkRegistryRunAsUser(*args: _Any) -> _Any:
	""" Checks if the provided runas user is valid.  True is return if the runas user is valid and false if it is not. """
	...

def checkRegistryUserPassword(*args: _Any) -> _Any:
	""" Check if the provided user and password authenticate in the registry. """
	...

def cleanupManagedNode(*args: _Any) -> _Any:
	""" Cleanup a managed node that no longer exists """
	...

def cleanupTarget(*args: _Any) -> _Any:
	""" Cleanup a Target that no longer exists """
	...

def clearAuthCache(*args: _Any) -> _Any:
	""" Clears the auth cache for a security domain; if no security domain is specified, the auth cache for the admin security domain will be cleared """
	...

def clearIdMgrRepositoryCache(*args: _Any) -> _Any:
	""" Clears the cache of the specified repository or of all repositories. """
	...

def clearIdMgrUserFromCache(*args: _Any) -> _Any:
	""" Removes a specified user from the cache. """
	...

def cloneDynamicCluster(*args: _Any) -> _Any:
	""" Use this command to clone a dynamic cluster. """
	...

def clonePreference(*args: _Any) -> _Any:
	""" Command to clone a user preference """
	...

def compareMultipleResourceAdapters(*args: _Any) -> _Any:
	""" Compare a list of multiple resource adapters to see if they are all able to be updated with the same RAR file. """
	...

def compareNodeVersion(*args: _Any) -> _Any:
	""" Compares the version of a given node with the specified version.  Only the number of levels in the specified version number are compared.  For example, if "6.0" compared to a node version of "6.0.1.0", they will compare as equal.  The possible return values are -1, 0, and 1. They are defined as follows: 
            - `-1`: node version is less than the specified version
            - `0`: node version is equal to the specified version
            - `1`: node version is greater than the specified version
    """
	...

def compareResourceAdapterToRAR(*args: _Any) -> _Any:
	""" Compare an existing Resource Adapter to a RAR file and determine whether the RAR is compatible for updating the Resource Adapter. """
	...

def configureAdminCustomUserRegistry(*args: _Any) -> _Any:
	""" Configure a custom user registry in the administrative security configuration """
	...

def configureAdminLDAPUserRegistry(*args: _Any) -> _Any:
	""" Configure an LDAP user registry in the administrative security configuration """
	...

def configureAdminLocalOSUserRegistry(*args: _Any) -> _Any:
	""" Configures a local OS user registry in the administrative security configuration. """
	...

def configureAdminWIMUserRegistry(*args: _Any) -> _Any:
	""" Configures a Federated repositories user registry in the administrative security configuration. """
	...

def configureAppCustomUserRegistry(*args: _Any) -> _Any:
	""" Configure a custom user registry in an application security domain """
	...

def configureAppLDAPUserRegistry(*args: _Any) -> _Any:
	""" Configures an LDAP user registry in an application security domain """
	...

def configureAppLocalOSUserRegistry(*args: _Any) -> _Any:
	""" Configures a local OS user registry in an application security domain. """
	...

def configureAppWIMUserRegistry(*args: _Any) -> _Any:
	""" Configures a Federated repositories user registry in an application security domain. """
	...

def configureAuthzConfig(*args: _Any) -> _Any:
	""" Configures an external authorization provider in global security or in an application security domain. """
	...

def configureCSIInbound(*args: _Any) -> _Any:
	""" Configures the CSI inbound information in the administrative security configuration or in an application security domain. """
	...

def configureCSIOutbound(*args: _Any) -> _Any:
	""" Configures the CSI outbound information in the administrative security configuration or in an application security domain. """
	...

def configureDVIPA(*args: _Any) -> _Any:
	""" configureDVIPA.desc """
	...

def configureInterceptor(*args: _Any) -> _Any:
	""" Configures an interceptor. """
	...

def configureJAASLoginEntry(*args: _Any) -> _Any:
	""" Configures a JAAS login module entry in the administrative security configuration or in an application security domain. """
	...

def configureJaspi(*args: _Any) -> _Any:
	""" Configure the Jaspi configuration. """
	...

def configureLoginModule(*args: _Any) -> _Any:
	""" Configures a login module in the administrative security configuration or in an application security domain. """
	...

def configureRSATokenAuthorization(*args: _Any) -> _Any:
	""" Command that modifies the role propagation authorization mechanism """
	...

def configureSingleHome(*args: _Any) -> _Any:
	""" configureDVIPA.desc """
	...

def configureSingleSignon(*args: _Any) -> _Any:
	""" Configure single signon. """
	...

def configureSpnego(*args: _Any) -> _Any:
	""" This command configures SPNEGO Web Authentication in the security configuration. """
	...

def configureTAM(*args: _Any) -> _Any:
	""" This command configures embedded Tivoli Access Manager on the WebSphere Application Server node or nodes specified. """
	...

def configureTAMTAI(*args: _Any) -> _Any:
	""" This command configures the embedded Tivoli Access Manager Trust Association Interceptor with classname TAMTrustAsociationInterceptorPlus. """
	...

def configureTAMTAIPdjrte(*args: _Any) -> _Any:
	""" This command performs the tasks necessary to fully configure the Tivoli Access Manager Runtime for Java. The specific tasks run are PDJrteCfg and SvrSslCfg. """
	...

def configureTAMTAIProperties(*args: _Any) -> _Any:
	""" This command adds the custom properties to the security configuration for the embedded Tivoli Access Manager Trust Association Interceptor with classname TAMTrustAsociationInterceptorPlus. """
	...

def configureTrustAssociation(*args: _Any) -> _Any:
	""" Configures a trust association. """
	...

def configureTrustedRealms(*args: _Any) -> _Any:
	""" Configures an inbound or outbound trusted realms. """
	...

def connectSIBWSEndpointListener(*args: _Any) -> _Any:
	""" Connect an endpoint listener to a service integration bus. """
	...

def convertCertForSecurityStandard(*args: _Any) -> _Any:
	""" Converts certificates used by SSL configuration and plugins so that they comply with specified FIPS level.  Also lists certificates that cannot be converted by WebSphere. """
	...

def convertFilterRefToString(*args: _Any) -> _Any:
	""" Converts an audit specification reference to a string representation. """
	...

def convertFilterStringToRef(*args: _Any) -> _Any:
	""" Converts an audit specification event and outcome to a reference representation. """
	...

def convertSSLCertificates(*args: _Any) -> _Any:
	""" Converts SSL personal certificates to a certificate that is created with the desired signature algorithm or lists SSL personal certificates that are not created with the desired signature algorithm. """
	...

def convertSSLConfig(*args: _Any) -> _Any:
	""" Converts old style SSL configuration to new style SSL configurations.  The CONVERT_SSLCONFIGS option will look for old style SSL configuration objects and change them to look like new style SSL configuration objects.  The CONVERT_TO_DEFAULT will go through make convert the whole SSL configuration to the new centralized SSL configuration style, removing the SSL configuraiton direct referencing from the servers. """
	...

def convertSelfSignedCertificatesToChained(*args: _Any) -> _Any:
	""" Converts self-signed certificates to chained certificate in a keystore, all keystore, or the default keystores.  The new chained certificate will be signed with root certificate specified or the default root if one is not specified.  All keystores in the configuration will be searched for the self-signed certificate's signer certificate and it will be replaced with the signer of the default root certificate. """
	...

def convertServerSecurityToSecurityDomain(*args: _Any) -> _Any:
	""" Task to convert server level security configuration to a security domain configuration. """
	...

def convertToSysplexNodeGroup(*args: _Any) -> _Any:
	""" Converts to a sysplex node group """
	...

def copyBinding(*args: _Any) -> _Any:
	""" The copyBinding command creates a copy of an existing binding. """
	...

def copyIdMgrFilesForDomain(*args: _Any) -> _Any:
	""" Copies the files related to virtual member manager from the specified source domain to the specified destination domain. """
	...

def copyPolicySet(*args: _Any) -> _Any:
	""" The copyPolicySet command creates a copy of an existing policy set. The default indicator is set to false for the new policy set. You may indicate whether to transfer attachments from the existing policy set to the new policy set. """
	...

def copyResourceAdapter(*args: _Any) -> _Any:
	""" copy the specified J2C resource adapter to the specified scope. """
	...

def copySecurityDomain(*args: _Any) -> _Any:
	""" Creates a security domain by coping from another security domain. """
	...

def copySecurityDomainFromGlobalSecurity(*args: _Any) -> _Any:
	""" Creates a security domain by copy the global administrative security configuration. """
	...

def correctSIBEnginePolicy(*args: _Any) -> _Any:
	""" Ensures that a messaging engines core group policy conforms to its associated bus members messaging engine assistance policy. """
	...

def createAllActivePolicy(*args: _Any) -> _Any:
	""" Create a policy that automatically activates all group members. """
	...

def createApacheServer(*args: _Any) -> _Any:
	""" Use this command to create an Apache Server. """
	...

def createApacheServerTemplate(*args: _Any) -> _Any:
	""" creates a server Template based on a server configuration """
	...

def createApplicationServer(*args: _Any) -> _Any:
	""" Command that creates a server """
	...

def createApplicationServerTemplate(*args: _Any) -> _Any:
	""" creates a server Template based on a server configuration """
	...

def createAuditEncryptionConfig(*args: _Any) -> _Any:
	""" Configures audit record encryption. """
	...

def createAuditEventFactory(*args: _Any) -> _Any:
	""" Creates an entry in the audit.xml to reference the configuration of an audit event factory implementation of the Audit Event Factory interface. """
	...

def createAuditFilter(*args: _Any) -> _Any:
	""" Creates an entry in the audit.xml to reference an Audit Specification. Enables the specification by default. """
	...

def createAuditKeyStore(*args: _Any) -> _Any:
	""" Creates a new Key Store. """
	...

def createAuditNotification(*args: _Any) -> _Any:
	""" Configures an audit notification. """
	...

def createAuditNotificationMonitor(*args: _Any) -> _Any:
	""" Configures an audit notification monitor. """
	...

def createAuditSelfSignedCertificate(*args: _Any) -> _Any:
	""" Create a new self-signed certificate and store it in a key store. """
	...

def createAuditSigningConfig(*args: _Any) -> _Any:
	""" Configures audit record signing. """
	...

def createAuthDataEntry(*args: _Any) -> _Any:
	""" Create an authentication data entry in the administrative security configuration or a in a security domain. """
	...

def createAuthorizationGroup(*args: _Any) -> _Any:
	""" Create a new authorization group. """
	...

def createBinaryEmitter(*args: _Any) -> _Any:
	""" Creates an entry in the audit.xml to reference the configuration of the Binary File Emitter implementation of the Service Provider interface. """
	...

def createCAClient(*args: _Any) -> _Any:
	""" Creates a certificate authority (CA) client configurator object. """
	...

def createCMSKeyStore(*args: _Any) -> _Any:
	""" Create a CMS KeyStore with password stash file. """
	...

def createCertificateRequest(*args: _Any) -> _Any:
	""" Create Certificate Request """
	...

def createChain(*args: _Any) -> _Any:
	""" Create a new chain of transport channels based on a chain template. """
	...
F
def createChainedCertificate(*args: _Any) -> _Any:
	""" Create a new chained certificate and store it in a key store. """
	...

def createCluster(*args: _Any) -> _Any:
	""" Creates a new application server cluster. """
	...

def createClusterMember(*args: _Any) -> _Any:
	""" Creates a new member of an application server cluster. """
	...

def createCoreGroup(*args: _Any) -> _Any:
	""" Create a new core group """
	...

def createCoreGroupAccessPoint(*args: _Any) -> _Any:
	""" This command creates a default core group access point for the specified core group and adds it to the default access point group. """
	...

def createDatasource(jdbc_provider: ConfigurationObjectName, datasource_config: _Union[str, list]) -> _Any:
	""" Create a new Datasource to access the backend data store.
	
	Application components use the Datasource to access connection instances to your database.
	A connection pool is associated with each Datasource. 
	
	Required parameters:
	- `-name`:
        The name of the data source. (String, required)
    - `-jndiName`:
        The Java Naming and Directory Interface (JNDI) name. (String, required)
    - `-dataStoreHelperClassName`:
        The name of the DataStoreHelper implementation class that extends the capabilities of the selected JDBC driver implementation class to perform data-specific functions. WebSphere® Application Server provides a set of DataStoreHelper implementation classes for each of the JDBC provider drivers it supports. (String, required)
        configureResourceProperties
        This command step configures the resource properties that are required by the data source. (Required) You can specify the following parameters for this step:
        - `name`:
        The name of the resource property. (String, required)
        - `type`:
        The type of the resource property. (String, required)
        - `value`:
        The value of the resource property. (String, required)

    Optional parameters:
    - `-description`:
        The description of the data source. (String, optional)
    - `-category`:
        The category that you can use to classify a group of data sources. (String, optional)
    - `-componentManagedAuthenticationAlias`:
        The alias used for database authentication at run time. This alias is only used when the application resource reference is using res-auth=Application. (String, optional)
    - `-containerManagedPersistence`:
        Specifies if the data source is used for container managed persistence for enterprise beans. The default value is true. (Boolean, optional)
    """
	...

def createDefaultARPWorkClass(*args: _Any) -> _Any:
	""" Creates default application routing policy work classes """
	...

def createDefaultASPWorkClass(*args: _Any) -> _Any:
	""" Creates default application service policy work classes """
	...

def createDefaultGRPWorkClass(*args: _Any) -> _Any:
	""" Creates a default generic server routing policy default work class """
	...

def createDefaultGSPWorkClass(*args: _Any) -> _Any:
	""" Creates a default generic server service policy default work class """
	...

def createDefaultSystemRPWorkClass(*args: _Any) -> _Any:
	""" Creates default system application routing policy work classes """
	...

def createDefaultSystemSPWorkClass(*args: _Any) -> _Any:
	""" Creates default system application service policy work classes """
	...

def createDescriptiveProp(*args: _Any) -> _Any:
	""" Create a descriptive property under an object. """
	...

def createDynamicCluster(*args: _Any) -> _Any:
	""" Create a new WAS dynamic cluster """
	...

def createDynamicClusterFromForeignServers(*args: _Any) -> _Any:
	""" Create a new dynamic cluster from existing foreign servers """
	...

def createDynamicClusterFromStaticCluster(*args: _Any) -> _Any:
	""" Create a new dynamic cluster from existing static cluster """
	...

def createDynamicSSLConfigSelection(*args: _Any) -> _Any:
	""" Create a Dynamic SSL configuration Selection. """
	...

def createElasticityAction(*args: _Any) -> _Any:
	""" Command to create a elasticity action """
	...

def createEmptyBLA(*args: _Any) -> _Any:
	""" Create a new business-level application with no composition units. """
	...

def createExtWasAppServer(*args: _Any) -> _Any:
	""" Command that creates a server """
	...

def createExtWasAppServerTemplate(*args: _Any) -> _Any:
	""" creates a server Template based on a server configuration """
	...

def createForeignServer(*args: _Any) -> _Any:
	""" Command that creates a server """
	...

def createForeignServerTemplate(*args: _Any) -> _Any:
	""" creates a server Template based on a server configuration """
	...

def createFullCheckpoint(*args: _Any) -> _Any:
	""" Create a full named checkpoint specified by the "checkpointName" """
	...

def createGenericServer(*args: _Any) -> _Any:
	""" Command that creates a server """
	...

def createGenericServerTemplate(*args: _Any) -> _Any:
	""" creates a server Template based on a server configuration """
	...

def createGroup(*args: _Any) -> _Any:
	""" Creates a group in the default realm. """
	...

def createHealthAction(*args: _Any) -> _Any:
	""" Command to create a health action """
	...

def createHealthPolicy(*args: _Any) -> _Any:
	""" Command to create a health policy """
	...

def createIdMgrCustomRepository(*args: _Any) -> _Any:
	""" Creates a custom repository configuration. """
	...

def createIdMgrDBRepository(*args: _Any) -> _Any:
	""" Creates a database repository configuration. """
	...

def createIdMgrFileRepository(*args: _Any) -> _Any:
	""" Creates a file repository configuration. """
	...

def createIdMgrLDAPRepository(*args: _Any) -> _Any:
	""" Creates an LDAP repository configuration object. """
	...

def createIdMgrRealm(*args: _Any) -> _Any:
	""" Creates a realm configuration. """
	...

def createIdMgrSupportedEntityType(*args: _Any) -> _Any:
	""" Creates a supported entity type configuration. """
	...

def createJ2CActivationSpec(*args: _Any) -> _Any:
	""" Create a J2C activation specification. """
	...

def createJ2CAdminObject(*args: _Any) -> _Any:
	""" Create a J2C administrative object. """
	...

def createJ2CConnectionFactory(*args: _Any) -> _Any:
	""" Create a J2C connection factory """
	...

def createJAXWSHandler(*args: _Any) -> _Any:
	""" Create a JAX-WS Handler """
	...

def createJAXWSHandlerList(*args: _Any) -> _Any:
	""" Create a JAX-WS Handler _List """
	...

def createJBossServer(*args: _Any) -> _Any:
	""" Command that creates a server """
	...

def createJBossServerTemplate(*args: _Any) -> _Any:
	""" creates a server Template based on a server configuration """
	...

def createJDBCProvider(*args: _Any) -> _Any:
	""" Create a new JDBC provider that is used to connect with a relational database for data access. """
	...

def createJobSchedulerProperty(*args: _Any) -> _Any:
	""" add a custom property for job scheduler """
	...

def createKeyManager(*args: _Any) -> _Any:
	""" Create a key manager. """
	...

def createKeyReference(*args: _Any) -> _Any:
	""" Create a Key Reference for a keySet. """
	...

def createKeySet(*args: _Any) -> _Any:
	""" Create a Key Set. """
	...

def createKeySetGroup(*args: _Any) -> _Any:
	""" Create a key set group. """
	...

def createKeyStore(*args: _Any) -> _Any:
	""" Creates a new keystore. """
	...

def createKrbAuthMechanism(*args: _Any) -> _Any:
	""" The KRB5 authentication mechanism security object field in the security configuration file is created based on the user input. """
	...

def createKrbConfigFile(*args: _Any) -> _Any:
	""" This command creates a Kerberos configuration file (krb5.ini or krb5.conf). """
	...

def createLMService(*args: _Any) -> _Any:
	""" Use the "createLMService" command to create a local mapping service, to which a service map can be attached. """
	...

def createLMServiceEventPoint(*args: _Any) -> _Any:
	""" Use the "createLMServiceEventPoint" command to create a local mapping service event point, in order to generate service mapping events. """
	...

def createLibertyServer(*args: _Any) -> _Any:
	""" Command that creates a server """
	...

def createLibertyServerTemplate(*args: _Any) -> _Any:
	""" creates a server Template based on a server configuration """
	...

def createLongRunningSchedulerProperty(*args: _Any) -> _Any:
	""" (Deprecated) add a custom property for long-running scheduler. Use createJobSchedulerProperty. """
	...

def createMOfNPolicy(*args: _Any) -> _Any:
	""" Create a policy that activates the specified number of group members. """
	...

def createManagedNodeGroup(*args: _Any) -> _Any:
	""" This command is used to create a group of managed nodes. (deprecated) """
	...

def createManagementScope(*args: _Any) -> _Any:
	""" Create a management scope. """
	...

def createMigrationReport(*args: _Any) -> _Any:
	""" Scans an application to create a Liberty migration report """
	...

def createMissingSIBEnginePolicy(*args: _Any) -> _Any:
	""" Create a core group policy for a messaging engine configured for server cluster bus member with messaging engine policy assistance enabled for the "Custom" policy. """
	...

def createNoOpPolicy(*args: _Any) -> _Any:
	""" Create a policy in which no group members are automatically activated. """
	...

def createNodeGroup(*args: _Any) -> _Any:
	""" create a node group """
	...

def createNodeGroupProperty(*args: _Any) -> _Any:
	""" add a custom property for a node group """
	...

def createNonWASDynamicCluster(*args: _Any) -> _Any:
	""" Create a new non-WAS dynamic cluster """
	...

def createOAuthProvider(*args: _Any) -> _Any:
	""" Create OAuth Provider """
	...

def createODRDynamicCluster(*args: _Any) -> _Any:
	""" Create On Demand Router dynamic cluster """
	...

def createObjectCacheInstance(*args: _Any) -> _Any:
	""" Create an Object Cache Instance.  An object cache instance is a location where an applications can store, distribute, and share data. """
	...

def createOnDemandRouter(*args: _Any) -> _Any:
	""" Command that creates a server """
	...

def createOnDemandRouterTemplate(*args: _Any) -> _Any:
	""" creates a server Template based on a server configuration """
	...

def createOneOfNPolicy(*args: _Any) -> _Any:
	""" Create a policy that keeps one member active at a time. """
	...

def createPHPDynamicCluster(*args: _Any) -> _Any:
	""" Create a new PHP dynamic cluster """
	...

def createPHPServer(*args: _Any) -> _Any:
	""" Use this command to create a PHP Server. """
	...

def createPHPServerTemplate(*args: _Any) -> _Any:
	""" Use this command to create a PHP Server template. """
	...

def createPolicySet(*args: _Any) -> _Any:
	""" The createPolicySet command creates a new policy set. Policy types are not created with the policy set. The default indicator is set to false. """
	...

def createPolicySetAttachment(*args: _Any) -> _Any:
	""" The createPolicySetAttachment command creates a new policy set attachment. """
	...

def createPropertiesFileTemplates(*args: _Any) -> _Any:
	""" Create properties file template for create/delete objects """
	...

def createProxyServer(*args: _Any) -> _Any:
	""" Command that creates a server """
	...

def createProxyServerTemplate(*args: _Any) -> _Any:
	""" creates a server Template based on a server configuration """
	...

def createRoutingPolicyWorkClass(*args: _Any) -> _Any:
	""" Use this command to create a Routing Policy Workclass """
	...

def createRoutingRules(*args: _Any) -> _Any:
	""" Use this command to create a routing policy rule list. """
	...

def createRuleset(*args: _Any) -> _Any:
	""" Use this command to create a ruleset. """
	...

def createSIBDestination(*args: _Any) -> _Any:
	""" Create bus destination. """
	...

def createSIBDestinations(*args: _Any) -> _Any:
	""" Create bus destinations. """
	...

def createSIBEngine(*args: _Any) -> _Any:
	""" Create a messaging engine. """
	...

def createSIBForeignBus(*args: _Any) -> _Any:
	""" Create a SIB foreign bus. """
	...

def createSIBJMSActivationSpec(*args: _Any) -> _Any:
	""" Create an activation specification in the SIB JMS resource adapter. """
	...

def createSIBJMSConnectionFactory(*args: _Any) -> _Any:
	""" Create a SIB JMS connection factory at the scope identified by the target object. """
	...

def createSIBJMSQueue(*args: _Any) -> _Any:
	""" Create a SIB JMS queue at the scope identified by the target object. """
	...

def createSIBJMSTopic(*args: _Any) -> _Any:
	""" Create a SIB JMS topic at the scope identified by the target object. """
	...

def createSIBLink(*args: _Any) -> _Any:
	""" Create a new SIB link. """
	...

def createSIBMQLink(*args: _Any) -> _Any:
	""" Create a new WebSphere MQ link. """
	...

def createSIBMediation(*args: _Any) -> _Any:
	""" Create a mediation. """
	...

def createSIBWMQServer(*args: _Any) -> _Any:
	""" Create a new WebSphere MQ server. """
	...

def createSIBWSEndpointListener(*args: _Any) -> _Any:
	""" Creates an endpoint listener configuration.This command is supported only in the connected mode. """
	...

def createSIBWSInboundService(*args: _Any) -> _Any:
	""" Create an inbound service. """
	...

def createSIBWSOutboundService(*args: _Any) -> _Any:
	""" Create an outbound service. """
	...

def createSIBus(*args: _Any) -> _Any:
	""" Create a bus. """
	...

def createSMFEmitter(*args: _Any) -> _Any:
	""" Creates an entry in the audit.xml to reference the configuration of an SMF Emitter implementation of the Service Provider interface. """
	...

def createSSLConfig(*args: _Any) -> _Any:
	""" Create a SSL Configuration. """
	...

def createSSLConfigGroup(*args: _Any) -> _Any:
	""" Create a SSL Configuration Group. """
	...

def createSSLConfigProperty(*args: _Any) -> _Any:
	""" Create a SSLConfig Property. """
	...

def createSecurityDomain(*args: _Any) -> _Any:
	""" Creates an empty security domain object. """
	...

def createSelfSignedCertificate(*args: _Any) -> _Any:
	""" Create a new self-signed certificate and store it in a keystore. """
	...

def createServerType(*args: _Any) -> _Any:
	""" Create a new Server Type e.g. (APPLICATION_SERVER) """
	...

def createServicePolicyWorkClass(*args: _Any) -> _Any:
	""" Use these commands to configure Service Policy Workclasses """
	...

def createServiceRules(*args: _Any) -> _Any:
	""" Use this command to create a service policy rule list. """
	...

def createServletCacheInstance(*args: _Any) -> _Any:
	""" Create a Servlet Cache Instance.  A servlet cache instance is a location where the dynamic cache can store, distribute, and share data. """
	...

def createStaticPolicy(*args: _Any) -> _Any:
	""" Create a policy that activates group members on all of the servers in the list. """
	...

def createSysplexNodeGroup(*args: _Any) -> _Any:
	""" create sysplex node group """
	...

def createSystemRoutingPolicyWorkClass(*args: _Any) -> _Any:
	""" Use this command to create a Routing Policy Workclass """
	...

def createSystemServicePolicyWorkClass(*args: _Any) -> _Any:
	""" Use this command to create a Routing Policy Workclass """
	...

def createTADataCollection(*args: _Any) -> _Any:
	""" This command scans the profile to create a Transformation Advisor data collection. """
	...

# --------------------------------------------------------------------------
@_overload
def createTCPEndPoint(target_object: _Literal['-interactive'], /) -> _Any:
    ...

@_overload
def createTCPEndPoint(target_object: ConfigurationObjectName, /) -> ConfigurationObjectName:
    ...

@_overload
def createTCPEndPoint(target_object: ConfigurationObjectName, options: _Union[str, _List[str]], /) -> ConfigurationObjectName:
    ...

def createTCPEndPoint(target_object: _Union[_Literal['-interactive'], ConfigurationObjectName], options: _Union[str, _List[str]], /) -> ConfigurationObjectName: # type: ignore[misc]
    """Create a new endpoint that you can associate with a TCP inbound channel.

    - If `options` is set to a string with value `"-interactive"`, the endpoint will 
        be created in _interactive mode_.

    Args:
        target_object (ConfigurationObjectName): Parent instance of the TransportChannelService that contains the TCPInboundChannel.
        options (str | list): String containing the `-name`, `-host` and `-port` parameters (all **required**) with their values set. 
            If `options` is set to a string with value `"-interactive"`, the endpoint will be created in _interactive mode_.

    Returns:
        ConfigurationObjectName: The object name of the endpoint that was created.

    Example:
        ```pycon
        >>> target = 'cells/mybuildCell01/nodes/mybuildCellManager01/servers/dmgr|server.xml#TransportChannelService_1'
        
        # As a string...
        >>> AdminTask.createTCPEndPoint(target, '[-name Sample_End_Pt_Name -host mybuild.location.ibm.com -port 8978]')
        
        # ... or as a list...
        >>> AdminTask.createTCPEndPoint(target, ['-name', 'Sample_End_Pt_Name', '-host', 'mybuild.location.ibm.com', '-port', '8978'])
        ```
    """
    ...
# --------------------------------------------------------------------------


def createTargetGroup(*args: _Any) -> _Any:
	""" This command is used to create a group of targets. """
	...

def createTemplateFromTemplate(*args: _Any) -> _Any:
	""" Create a server template from an existing server template """
	...

def createThirdPartyEmitter(*args: _Any) -> _Any:
	""" Creates an entry in the audit.xml to reference the configuration of a Third Party Emitter implementation of the Service Provider interface. """
	...

def createTomCatServer(*args: _Any) -> _Any:
	""" Command that creates a server """
	...

def createTomCatServerTemplate(*args: _Any) -> _Any:
	""" creates a server Template based on a server configuration """
	...

def createTrustManager(*args: _Any) -> _Any:
	""" Create a trust Manager. """
	...

def createUDPEndPoint(*args: _Any) -> _Any:
	""" Create a new NamedEndPoint endpoint to associate with a UDPInboundChannel """
	...

def createUnmanagedNode(*args: _Any) -> _Any:
	""" Use this command to create an unmanaged node in a cell. """
	...

def createUser(*args: _Any) -> _Any:
	""" Creates a PersonAccount in the default realm. """
	...

def createWMQActivationSpec(*args: _Any) -> _Any:
	""" Creates a IBM MQ Activation Specification at the scope provided to the command. """
	...

def createWMQConnectionFactory(*args: _Any) -> _Any:
	""" Creates a IBM MQ Connection Factory at the scope provided to the command. """
	...

def createWMQQueue(*args: _Any) -> _Any:
	""" Creates a IBM MQ Queue at the scope provided to the command. """
	...

def createWMQTopic(*args: _Any) -> _Any:
	""" Creates a IBM MQ Topic at the scope provided to the command. """
	...

def createWSCertExpMonitor(*args: _Any) -> _Any:
	""" Create a certificate expiration monitor. """
	...

def createWSGWGatewayService(*args: _Any) -> _Any:
	""" createWSGWGatewayService.description """
	...

def createWSGWProxyService(*args: _Any) -> _Any:
	""" createWSGWProxyService.description """
	...

def createWSNAdministeredSubscriber(*args: _Any) -> _Any:
	""" Add an administered subscriber to a WS-Notification service point """
	...

def createWSNService(*args: _Any) -> _Any:
	""" Create a WS-Notification service """
	...

def createWSNServicePoint(*args: _Any) -> _Any:
	""" Create a WS-Notification service point """
	...

def createWSNTopicDocument(*args: _Any) -> _Any:
	""" Add an instance document to a WS-Notification topic namespace """
	...

def createWSNTopicNamespace(*args: _Any) -> _Any:
	""" Create a WS-Notification topic namespace """
	...

def createWSNotifier(*args: _Any) -> _Any:
	""" Create a notifier. """
	...

def createWSSchedule(*args: _Any) -> _Any:
	""" Create a schedule. """
	...

def createWasCEServer(*args: _Any) -> _Any:
	""" Use this command to create an WebSphere Community Edition Server. """
	...

def createWasCEServerTemplate(*args: _Any) -> _Any:
	""" creates a server Template based on a server configuration """
	...

def createWebLogicServer(*args: _Any) -> _Any:
	""" Command that creates a server """
	...

def createWebLogicServerTemplate(*args: _Any) -> _Any:
	""" creates a server Template based on a server configuration """
	...

def createWebModuleProxyConfig(*args: _Any) -> _Any:
	""" Create a proxy configuration for a Web module """
	...

def createWebServer(*args: _Any) -> _Any:
	""" Command that creates a server """
	...

def createWebServerByHostName(*args: _Any) -> _Any:
	""" Create Web server definition using hostname. """
	...

def createWebServerTemplate(*args: _Any) -> _Any:
	""" creates a server Template based on a server configuration """
	...

def deactivateEdition(*args: _Any) -> _Any:
	""" Marks the state of an edition as INACTIVE. """
	...

def defineJaspiProvider(*args: _Any) -> _Any:
	""" Define a new authentication provider. """
	...

def deleteAsset(*args: _Any) -> _Any:
	""" Delete an asset which was imported into the product configuration repository. """
	...

def deleteAttachmentsForPolicySet(*args: _Any) -> _Any:
	""" The deleteAttachmentsForPolicySet command removes all attachments for a specific policy set. """
	...

def deleteAuditCertificate(*args: _Any) -> _Any:
	""" Delete the personal certificate used for audit encryption from the keystore identified as the audit encryption keystore """
	...

def deleteAuditEmitterByName(*args: _Any) -> _Any:
	""" Deletes an audit emitter implementation object by unique name. """
	...

def deleteAuditEmitterByRef(*args: _Any) -> _Any:
	""" Deletes an audit emitter implementation object by reference id. """
	...

def deleteAuditEncryptionConfig(*args: _Any) -> _Any:
	""" Deletes the audit record encryption configuration. """
	...

def deleteAuditEventFactoryByName(*args: _Any) -> _Any:
	""" Deletes the audit event factory specified by the unique name. """
	...

def deleteAuditEventFactoryByRef(*args: _Any) -> _Any:
	""" Deletes the audit event factory specified by the reference id. """
	...

def deleteAuditFilter(*args: _Any) -> _Any:
	""" Deletes an audit specification entry in the audit.xml that matches the event and outcome. """
	...

def deleteAuditFilterByRef(*args: _Any) -> _Any:
	""" Deletes an audit specification entry in the audit.xml that matches the reference Id. """
	...

def deleteAuditKeyStore(*args: _Any) -> _Any:
	""" Deletes an existing Key Store. """
	...

def deleteAuditNotification(*args: _Any) -> _Any:
	""" Deletes an audit notification. """
	...

def deleteAuditNotificationMonitorByName(*args: _Any) -> _Any:
	""" Deletes an audit notification monitor specified by the unique name. """
	...

def deleteAuditNotificationMonitorByRef(*args: _Any) -> _Any:
	""" Deletes an audit notification monitor specified by the reference id. """
	...

def deleteAuditSigningConfig(*args: _Any) -> _Any:
	""" Unconfigures audit record signing. """
	...

def deleteAuthDataEntry(*args: _Any) -> _Any:
	""" Delete an authentication data entry from the administrative security configuration or a in a security domain. """
	...

def deleteAuthorizationGroup(*args: _Any) -> _Any:
	""" Delete an existing authorization group """
	...

def deleteBLA(*args: _Any) -> _Any:
	""" Delete a specified business-level application. """
	...

def deleteCAClient(*args: _Any) -> _Any:
	""" Deletes a certificate authority (CA) client configurator object. """
	...

def deleteCertificate(*args: _Any) -> _Any:
	""" Delete a personal certificate from a keystore. """
	...

def deleteCertificateRequest(*args: _Any) -> _Any:
	""" Delete an existing certificate request from a keystore. """
	...

def deleteChain(*args: _Any) -> _Any:
	""" Delete an existing chain and, optionally, the transport channels in the chain. """
	...

def deleteCheckpoint(*args: _Any) -> _Any:
	""" Delete the named checkpoint specified by the "checkpointName" """
	...

def deleteCluster(*args: _Any) -> _Any:
	""" Delete the configuration of an application server cluster. """
	...

def deleteClusterMember(*args: _Any) -> _Any:
	""" Deletes a member from an application server cluster. """
	...

def deleteCompUnit(*args: _Any) -> _Any:
	""" Delete a composition unit from a business-level application. """
	...

def deleteConfigProperties(*args: _Any) -> _Any:
	""" Delete configuration specified in properties file """
	...

def deleteCoreGroup(*args: _Any) -> _Any:
	""" Delete an existing core group. The core group must contain no servers. """
	...

def deleteCoreGroupAccessPoints(*args: _Any) -> _Any:
	""" Delete all the core group access points associated with a specified core group. """
	...

def deleteDatasource(*args: _Any) -> _Any:
	""" Delete a Datasource used to access a relational database. """
	...

def deleteDescriptiveProp(*args: _Any) -> _Any:
	""" Delete a descriptive property under an object. """
	...

def deleteDynamicCluster(*args: _Any) -> _Any:
	""" Delete a dynamic cluster from the configuration repository. """
	...

def deleteDynamicSSLConfigSelection(*args: _Any) -> _Any:
	""" Delete an existing Dynamic SSL configuration Selection. """
	...

def deleteElasticityAction(*args: _Any) -> _Any:
	""" Command to delete a elasticity action """
	...

def deleteGroup(*args: _Any) -> _Any:
	""" Deletes a group from the default realm. """
	...

def deleteHealthAction(*args: _Any) -> _Any:
	""" Command to delete a health action """
	...

def deleteHealthPolicy(*args: _Any) -> _Any:
	""" Command to delete a health policy """
	...

def deleteIdMgrDBTables(*args: _Any) -> _Any:
	""" Deletes the tables of the database in virtual member manager. """
	...

def deleteIdMgrEntryMappingRepositoryTables(*args: _Any) -> _Any:
	""" Deletes the tables of the entry mapping database in virtual member manager. """
	...

def deleteIdMgrLDAPAttr(*args: _Any) -> _Any:
	""" Deletes a LDAP attribute configuration data for a specified entity type for a specific LDAP repository. Use the name of either the LDAP attribute or virtual member manager property. """
	...

def deleteIdMgrLDAPAttrNotSupported(*args: _Any) -> _Any:
	""" Deletes the configuration for a virtual member manager property not supported by a specific LDAP repository. """
	...

def deleteIdMgrLDAPEntityType(*args: _Any) -> _Any:
	""" Deletes a LDAP entity type configuration data for a specified entity type for a specific LDAP repository. """
	...

def deleteIdMgrLDAPEntityTypeRDNAttr(*args: _Any) -> _Any:
	""" Deletes RDN attribute configuration from an LDAP entity type configuration. """
	...

def deleteIdMgrLDAPExternalIdAttr(*args: _Any) -> _Any:
	""" Deletes the configuration for an LDAP attribute used as an external ID. """
	...

def deleteIdMgrLDAPGroupConfig(*args: _Any) -> _Any:
	""" Deletes the entire LDAP group configuration. """
	...

def deleteIdMgrLDAPGroupDynamicMemberAttr(*args: _Any) -> _Any:
	""" Deletes the dynamic member attribute configuration from the LDAP group configuration. """
	...

def deleteIdMgrLDAPGroupMemberAttr(*args: _Any) -> _Any:
	""" Deletes the member attribute configuration from the LDAP group configuration. """
	...

def deleteIdMgrLDAPServer(*args: _Any) -> _Any:
	""" Deletes the primary LDAP server and configured backup servers. """
	...

def deleteIdMgrPropertyExtensionEntityData(*args: _Any) -> _Any:
	""" Deletes the property data from the property extension repository. It also deletes any entity IDs with which there is no property data associated, from the property extension repository in virtual member manager. """
	...

def deleteIdMgrPropertyExtensionRepositoryTables(*args: _Any) -> _Any:
	""" Deletes the tables of the property extension database in virtual member manager. """
	...

def deleteIdMgrRealm(*args: _Any) -> _Any:
	""" Deletes the specified realm configuration. """
	...

def deleteIdMgrRealmBaseEntry(*args: _Any) -> _Any:
	""" Deletes a base entry from a specified realm configuration. """
	...

def deleteIdMgrRealmDefaultParent(*args: _Any) -> _Any:
	""" Deletes the default parent of an entity type for a realm. If * is specified as entityTypeName, default parent mapping for all entity types is deleted. If the realm name is not specified, default realm is used. """
	...

def deleteIdMgrRepository(*args: _Any) -> _Any:
	""" Deletes the configuration of the specified repository. """
	...

def deleteIdMgrRepositoryBaseEntry(*args: _Any) -> _Any:
	""" Deletes a base entry from the specified repository. """
	...

def deleteIdMgrSupportedEntityType(*args: _Any) -> _Any:
	""" Deletes a supported entity type configuration. """
	...

def deleteJAXWSHandler(*args: _Any) -> _Any:
	""" Delete a JAX-WS Handler """
	...

def deleteJAXWSHandlerList(*args: _Any) -> _Any:
	""" Delete a JAX-WS Handler _List """
	...

def deleteJDBCProvider(*args: _Any) -> _Any:
	""" Delete a JDBC provider that is used to connect to a relational database for data access. """
	...

def deleteJob(*args: _Any) -> _Any:
	""" Deletes a previously submitted job. """
	...

def deleteKeyManager(*args: _Any) -> _Any:
	""" Delete a key manager. """
	...

def deleteKeyReference(*args: _Any) -> _Any:
	""" Delete an existing Key Reference from a keySet. """
	...

def deleteKeySet(*args: _Any) -> _Any:
	""" Delete a key set. """
	...

def deleteKeySetGroup(*args: _Any) -> _Any:
	""" Delete a key set group. """
	...

def deleteKeyStore(*args: _Any) -> _Any:
	""" Deletes an existing keystore. """
	...

def deleteKrbAuthMechanism(*args: _Any) -> _Any:
	""" The KRB5 authentication mechanism security object field in the security configuration file is deleted. """
	...

def deleteLMService(*args: _Any) -> _Any:
	""" Use the "deleteLMService" command to delete an existing local mapping service. """
	...

def deleteLMServiceEventPoint(*args: _Any) -> _Any:
	""" Use the "deleteLMServiceEventPoint" command to delete a local mapping service event point. """
	...

def deleteManagedNodeGroup(*args: _Any) -> _Any:
	""" This command is used to delete a group of managed nodes. (deprecated) """
	...

def deleteManagementScope(*args: _Any) -> _Any:
	""" Delete an existing management scope. """
	...

def deleteMemberFromManagedNodeGroup(*args: _Any) -> _Any:
	""" This command is used to delete members from a group of managed nodes. (deprecated) """
	...

def deleteMemberFromTargetGroup(*args: _Any) -> _Any:
	""" This command is used to delete members from a target group. """
	...

def deleteMigrationReport(*args: _Any) -> _Any:
	""" Deletes a Liberty migration report for an application """
	...

def deleteOAuthProvider(*args: _Any) -> _Any:
	""" Delete OAuth Provider """
	...

def deletePasswordEncryptionKey(*args: _Any) -> _Any:
	""" Deletes an AES encryption key from the keystore file. This command is disabled when the custom KeyManager class is used. """
	...

def deletePolicy(*args: _Any) -> _Any:
	""" Delete a policy that matches the provided policy name. """
	...

def deletePolicySet(*args: _Any) -> _Any:
	""" The deletePolicySet command deletes the specified policy set. If attachments exist for the policy set, the command returns a failure message. """
	...

def deletePolicySetAttachment(*args: _Any) -> _Any:
	""" The deletePolicySetAttachment command removes a policy set attachment. """
	...

def deletePolicyType(*args: _Any) -> _Any:
	""" The deletePolicyType command deletes a policy type from a policy set. """
	...

def deleteRemoteCellFromIntelligentManagement(*args: _Any) -> _Any:
	""" deleteRemoteCellFromIntellMgmtDesc """
	...

def deleteRoutingPolicyWorkClass(*args: _Any) -> _Any:
	""" Use this command to delete a Routing Policy Workclass """
	...

def deleteSAMLIdpPartner(*args: _Any) -> _Any:
	""" This command removes the SAML TAI IdP partner from the security configuration. """
	...

def deleteSAMLTAISSO(*args: _Any) -> _Any:
	""" This command removes the SAML TAI SSO from the security configuration. """
	...

def deleteSCClientCacheConfigurationCustomProperties(*args: _Any) -> _Any:
	""" Delete the Custom property """
	...

def deleteSIBDestination(*args: _Any) -> _Any:
	""" Delete bus destination. """
	...

def deleteSIBDestinations(*args: _Any) -> _Any:
	""" Delete bus destinations. """
	...

def deleteSIBEngine(*args: _Any) -> _Any:
	""" Delete the default engine or named engine from the target bus. """
	...

def deleteSIBForeignBus(*args: _Any) -> _Any:
	""" Delete a SIB foreign bus. """
	...

def deleteSIBJMSActivationSpec(*args: _Any) -> _Any:
	""" Delete given SIB JMS activation specification. """
	...

def deleteSIBJMSConnectionFactory(*args: _Any) -> _Any:
	""" Delete the supplied SIB JMS connection factory. """
	...

def deleteSIBJMSQueue(*args: _Any) -> _Any:
	""" Delete the supplied SIB JMS queue. """
	...

def deleteSIBJMSTopic(*args: _Any) -> _Any:
	""" Delete the supplied SIB JMS topic. """
	...

def deleteSIBLink(*args: _Any) -> _Any:
	""" Delete a SIB link. """
	...

def deleteSIBMQLink(*args: _Any) -> _Any:
	""" Delete an WebSphere MQ link. """
	...

def deleteSIBMQLinkReceiverChannel(*args: _Any) -> _Any:
	""" This command deletes the Receiver Channel associated with the SIB MQ Link passed in as a target object. """
	...

def deleteSIBMQLinkSenderChannel(*args: _Any) -> _Any:
	""" This command deletes the Sender Channel associated with the SIB MQ Link passed in as a target object. """
	...

def deleteSIBMediation(*args: _Any) -> _Any:
	""" Delete a mediation. """
	...

def deleteSIBWMQServer(*args: _Any) -> _Any:
	""" Delete a named WebSphere MQ server. Also, delete its membership of any buses, and cleanup all associated configuration. """
	...

def deleteSIBWSEndpointListener(*args: _Any) -> _Any:
	""" Delete an endpoint listener. """
	...

def deleteSIBWSInboundService(*args: _Any) -> _Any:
	""" Delete an inbound service. """
	...

def deleteSIBWSOutboundService(*args: _Any) -> _Any:
	""" Delete an outbound service. """
	...

def deleteSIBus(*args: _Any) -> _Any:
	""" Delete a named bus, including everything on it. """
	...

def deleteSSLConfig(*args: _Any) -> _Any:
	""" Delete an existing SSL configuration. """
	...

def deleteSSLConfigGroup(*args: _Any) -> _Any:
	""" Delete a SSLConfig group. """
	...

def deleteSSLConfigProperty(*args: _Any) -> _Any:
	""" Delete a SSLConfig Property. """
	...

def deleteSTSProperty(*args: _Any) -> _Any:
	""" Remove a configuration property under a configuration group. """
	...

def deleteSTSTokenTypeConfigurationCustomProperties(*args: _Any) -> _Any:
	""" Delete custom properties from the configuration of a token type. """
	...

def deleteSecurityDomain(*args: _Any) -> _Any:
	""" Deletes a domain object. """
	...

def deleteServer(*args: _Any) -> _Any:
	""" Delete a server configuration """
	...

def deleteServerTemplate(*args: _Any) -> _Any:
	""" A command that Deletes a Server Template """
	...

def deleteServicePolicyWorkClass(*args: _Any) -> _Any:
	""" Use this command to delete a Service Policy Workclass """
	...

def deleteSignerCertificate(*args: _Any) -> _Literal['']:
	""" Delete a signer certificate from a keystore. """
	...

def deleteSpnegoFilter(*args: _Any) -> _Any:
	""" This command removes SPNEGO Web authentication Filter from the security configuration. If a host name is not specified, all the SPNEGO Web authentication Filters are removed. """
	...

def deleteSpnegoTAIProperties(*args: _Any) -> _Any:
	""" This command removes SPNEGO TAI properties from the security configuration. If an spnId is not specified, all the SPNEGO TAI properties are removed. """
	...

def deleteTADataCollection(*args: _Any) -> _Any:
	""" This command deletes the previously generated Transformation Advisor data collection. """
	...

def deleteTargetGroup(*args: _Any) -> _Any:
	""" This command is used to delete a group of targets. """
	...

def deleteTrustManager(*args: _Any) -> _Any:
	""" Delete a trust manager. """
	...

def deleteUser(*args: _Any) -> _Any:
	""" Deletes a PersonAccount from the default realm. """
	...

def deleteWMQActivationSpec(*args: _Any) -> _Any:
	""" Deletes the IBM MQ Activation Specification object provided to the command. """
	...

def deleteWMQConnectionFactory(*args: _Any) -> _Any:
	""" Deletes the IBM MQ Connection Factory object provided to the command. """
	...

def deleteWMQQueue(*args: _Any) -> _Any:
	""" Deletes the IBM MQ Queue object provided to the command. """
	...

def deleteWMQTopic(*args: _Any) -> _Any:
	""" Deletes the IBM MQ Topic object provided to the command. """
	...

def deleteWSCertExpMonitor(*args: _Any) -> _Any:
	""" Specifies the certificate expiration monitor name. """
	...

def deleteWSGWGatewayService(*args: _Any) -> _Any:
	""" deleteWSGWGatewayService.description """
	...

def deleteWSGWInstance(*args: _Any) -> _Any:
	""" deleteWSGWInstance.description """
	...

def deleteWSGWProxyService(*args: _Any) -> _Any:
	""" deleteWSGWProxyService.description """
	...

def deleteWSNAdministeredSubscriber(*args: _Any) -> _Any:
	""" Remove an administered subscriber from a WS-Notification service point """
	...

def deleteWSNService(*args: _Any) -> _Any:
	""" Delete a WS-Notification service """
	...

def deleteWSNServicePoint(*args: _Any) -> _Any:
	""" Delete a WS-Notification service point """
	...

def deleteWSNTopicDocument(*args: _Any) -> _Any:
	""" Remove an instance document from a WS-Notification topic namespace """
	...

def deleteWSNTopicNamespace(*args: _Any) -> _Any:
	""" Delete a WS-Notification topic namespace """
	...

def deleteWSNotifier(*args: _Any) -> _Any:
	""" Delete an existing notifier. """
	...

def deleteWSSDistributedCacheConfigCustomProperties(*args: _Any) -> _Any:
	""" Remove Web Services Security distributed cache custom properties """
	...

def deleteWSSchedule(*args: _Any) -> _Any:
	""" Delete an existing schedule. """
	...

def deleteWebModuleProxyConfig(*args: _Any) -> _Any:
	""" Delete the proxy server configuration for a Web module """
	...

def deleteWebServer(*args: _Any) -> _Any:
	""" Delete a server configuration """
	...

def deployWasCEApp(*args: _Any) -> _Any:
	""" Use this command to deploy a WAS CE application onto a server. """
	...

def detachServiceMap(*args: _Any) -> _Any:
	""" Use the "detachServiceMap" command to detach a service map from a local mapping service. """
	...

def disableAudit(*args: _Any) -> _Any:
	""" Disables Security Auditing and resets the auditEnabled field in audit.xml. """
	...

def disableAuditEncryption(*args: _Any) -> _Any:
	""" Disables audit encryption. """
	...

def disableAuditFilter(*args: _Any) -> _Any:
	""" Disables the Audit Specification. """
	...

def disableAuditSigning(*args: _Any) -> _Any:
	""" Disables audit signing. """
	...

def disableIntelligentManagement(*args: _Any) -> _Any:
	""" Command to disable Intelligent Management """
	...

def disableLMServiceEventPoint(*args: _Any) -> _Any:
	""" Use the "disableLMServiceEventPoint" command to disable a local mapping service event point, in order to stop generation of service mapping events. """
	...

def disablePasswordEncryption(*args: _Any) -> _Any:
	""" Disables the configuration of the password encryption. As a result, the values of xor or custom are used for the encryption algorithm. """
	...

def disableProvisioning(*args: _Any) -> _Any:
	""" Disable provisioning on a server. All components will be started. """
	...

def disableServerPort(*args: _Any) -> _Any:
	""" Disable all the transport chains associated with an endpoint on a server. Returns a list of all the disabled transport chains on successful execution of the command. """
	...

def disableVerboseAudit(*args: _Any) -> _Any:
	""" Disables the verbose gathering of audit data. """
	...

def disconnectSIBWSEndpointListener(*args: _Any) -> _Any:
	""" Disconnect an endpoint listener from a service integration bus. """
	...

def displayJaspiProvider(*args: _Any) -> _Any:
	""" Display configuration data for the given authentication provider(s). """
	...

def displayJaspiProviderNames(*args: _Any) -> _Any:
	""" Display the names of all authentication providers in the security configuration. """
	...

def doesCoreGroupExist(*args: _Any) -> _Any:
	""" Check to see if a core group exists. """
	...

def dpAddAppliance(*args: _Any) -> _Any:
	""" Use the dpAddAppliance command to add an appliance to the DataPower appliance manager. """
	...

def dpAddFirmwareVersion(*args: _Any) -> _Any:
	""" Use the dpAddFirmwareVersion command to add a firmware version to the DataPower appliance manager. """
	...

def dpAddManagedSet(*args: _Any) -> _Any:
	""" Use the dpAddManagedSet command to add a managed set to the DataPower appliance manager. """
	...

def dpCopyMSDomainVersion(*args: _Any) -> _Any:
	""" Use the dpCopyMSDomainVersion command to copy a DataPower appliance manager managed domain version to a new managed set. """
	...

def dpCopyMSSettingsVersion(*args: _Any) -> _Any:
	""" Use the dpCopyMSSettingsVersion command to copy a DataPower appliance manager managed settings version to a new managed set. """
	...

def dpExport(*args: _Any) -> _Any:
	""" Use the dpExport command to export the DataPower appliance manager configuration and versions. """
	...

def dpGetAllApplianceIds(*args: _Any) -> _Any:
	""" Use the dpGetAllApplianceIds command to get the IDs of each appliance in the DataPower appliance manager. """
	...

def dpGetAllDomainNames(*args: _Any) -> _Any:
	""" Use the dpGetAllDomainNames command to get the names of each of the domains on a DataPower appliance. """
	...

def dpGetAllFirmwareIds(*args: _Any) -> _Any:
	""" Use the dpGetAllFirmwareIds command to get the IDs of each DataPower appliance manager firmware in the configuration. """
	...

def dpGetAllFirmwareVersionIds(*args: _Any) -> _Any:
	""" Use the dpGetAllFirmwareVersionIds command to get the IDs of each DataPower appliance manager firmware version. """
	...

def dpGetAllMSApplianceIds(*args: _Any) -> _Any:
	""" Use the dpGetAllMSApplianceIds command to get the IDs of each appliance in a DataPower appliance manager managed set. """
	...

def dpGetAllMSDomainIds(*args: _Any) -> _Any:
	""" Use the dpGetAllMSDomainIds command to get the IDs of each domain in a DataPower appliance manager managed set. """
	...

def dpGetAllMSDomainVersionIds(*args: _Any) -> _Any:
	""" Use the dpGetAllMSDomainVersionIds command to get the IDs of each domain version in a DataPower appliance manager managed set. """
	...

def dpGetAllMSIdsUsingFirmwareVersion(*args: _Any) -> _Any:
	""" Use the dpGetAllMSIdsUsingFirmwareVersion command to get the IDs of the managed sets that use a firmware version. """
	...

def dpGetAllMSSettingsVersionIds(*args: _Any) -> _Any:
	""" Use the dpGetAllMSSettingsVersionIds command to get the IDs of each settings version in a DataPower appliance manager managed set. """
	...

def dpGetAllManagedSetIds(*args: _Any) -> _Any:
	""" Use the dpGetAllManagedSetIds command to get the IDs of each DataPower appliance manager managed set. """
	...

def dpGetAllTaskIds(*args: _Any) -> _Any:
	""" Use the dpGetAllTaskIDs command to get the IDs of each of the DataPower appliance manager tasks. """
	...

def dpGetAppliance(*args: _Any) -> _Any:
	""" Use the dpGetAppliance command to get a specific appliance in the DataPower appliance manager. """
	...

def dpGetBestFirmware(*args: _Any) -> _Any:
	""" Use the dpGetBestFirmware command to get the firmware that best matches the parameters. """
	...

def dpGetFirmware(*args: _Any) -> _Any:
	""" Use the dpGetFirmware command to get a specific DataPower appliance manager firmware. """
	...

def dpGetFirmwareVersion(*args: _Any) -> _Any:
	""" Use the dpGetFirmwareVersion command to get a specific DataPower appliance manager firmware version. """
	...

def dpGetMSDomain(*args: _Any) -> _Any:
	""" Use the dpGetMSDomain command to get a DataPower appliance manager managed domain. """
	...

def dpGetMSDomainVersion(*args: _Any) -> _Any:
	""" Use the dpGetMSDomainVersion command to get a DataPower appliance manager managed domain version. """
	...

def dpGetMSSettings(*args: _Any) -> _Any:
	""" Use the dpGetMSSettings command to get the DataPower appliance manager managed settings. """
	...

def dpGetMSSettingsVersion(*args: _Any) -> _Any:
	""" Use the dpGetMSSettingsVersion command to get a DataPower appliance manager managed settings version. """
	...

def dpGetManagedSet(*args: _Any) -> _Any:
	""" Use the dpGetManagedSet comand to get a DataPower appliance manager managed set. """
	...

def dpGetManager(*args: _Any) -> _Any:
	""" Use the dpGetManager command to get the properties of the DataPower appliance manager. """
	...

def dpGetManagerStatus(*args: _Any) -> _Any:
	""" Use the dpGetManagerStatus command to get the status of the DataPower appliance manager. """
	...

def dpGetTask(*args: _Any) -> _Any:
	""" Use the dpGetTask command to get a specific DataPower appliance manager task. """
	...

def dpImport(*args: _Any) -> _Any:
	""" Use the dpImport command to import the DataPower appliance manager configuration and versions. """
	...

def dpManageAppliance(*args: _Any) -> _Any:
	""" Use the dpManageAppliance command to add the appliance to a managed set and to start managing the appliance. """
	...

def dpManageDomain(*args: _Any) -> _Any:
	""" Use the dpManageDomain command to add the domain to a managed set, and to start managing the domain. """
	...

def dpPurgeTask(*args: _Any) -> _Any:
	""" Use the dpPurgeTask command to purge a DataPower appliance manager task. """
	...

def dpRemoveAppliance(*args: _Any) -> _Any:
	""" Use the dpRemoveAppliance command to remove an appliance from the DataPower appliance manager. """
	...

def dpRemoveFirmwareVersion(*args: _Any) -> _Any:
	""" Use the dpRemoveFirmwareVersion command to remove a firmware version from the DataPower appliance manager. """
	...

def dpRemoveMSDomainVersion(*args: _Any) -> _Any:
	""" Use the dpRemoveMSDomainVersion command to remove a managed domain version from the DataPower appliance manager. """
	...

def dpRemoveMSSettingsVersion(*args: _Any) -> _Any:
	""" Use the dpRemoveMSSettingsVersion command to remove a managed settings version from the DataPower appliance manager. """
	...

def dpRemoveManagedSet(*args: _Any) -> _Any:
	""" Use the dpRemoveManagedSet command to remove a managed set from the DataPower appliance manager. """
	...

def dpSetAppliance(*args: _Any) -> _Any:
	""" Use the dpSetAppliance command to modify an appliance in the DataPower appliance manager. """
	...

def dpSetFirmwareVersion(*args: _Any) -> _Any:
	""" Use the dpSetFirmwareVersion command to modify a DataPower appliance manager firmware version. """
	...

def dpSetMSDomain(*args: _Any) -> _Any:
	""" Use the dpSetMSDomain command to modify a DataPower appliance manager managed domain. """
	...

def dpSetMSDomainVersion(*args: _Any) -> _Any:
	""" Use the dpSetMSDomainVersion command to modify a DataPower appliance manager managed domain version. """
	...

def dpSetMSSettings(*args: _Any) -> _Any:
	""" Use the dpSetMSSettings command to modify the DataPower appliance manager managed settings. """
	...

def dpSetMSSettingsVersion(*args: _Any) -> _Any:
	""" Use the dpSetMSSettingsVersion command to modify a DataPower appliance manager managed settings version. """
	...

def dpSetManagedSet(*args: _Any) -> _Any:
	""" Use the dpSetManagedSet command to modify a DataPower appliance manager managed set. """
	...

def dpSetManager(*args: _Any) -> _Any:
	""" Use the dpSetManager command to modify the DataPower appliance manager. """
	...

def dpStopManager(*args: _Any) -> _Any:
	""" Use the dpStopManager command to stop the DataPower appliance manager. """
	...

def dpSynchManagedSet(*args: _Any) -> _Any:
	""" Use the dpSynchManagedSet command to manually synchronize a DataPower appliance manager managed set. """
	...

def dpUnmanageAppliance(*args: _Any) -> _Any:
	""" Use the dpUnmanageAppliance command to remove the appliance of interest from its managed set, and to stop managing the appliance. """
	...

def dpUnmanageDomain(*args: _Any) -> _Any:
	""" Use the dpUnmanageDomain command to remove the domain from the managed set, and to stop managing the domain. """
	...

def duplicateMembershipOfGroup(*args: _Any) -> _Any:
	""" Makes a group a member of the same groups as another group. """
	...

def duplicateMembershipOfUser(*args: _Any) -> _Any:
	""" Makes a user a member of the same groups as another user. """
	...

def editAsset(*args: _Any) -> _Any:
	""" Edit options specified when a specified asset was imported. """
	...

def editBLA(*args: _Any) -> _Any:
	""" Edit options for a specified business-level application. """
	...

def editCompUnit(*args: _Any) -> _Any:
	""" Edit options for a specified composition unit. """
	...

def editSTSProperty(*args: _Any) -> _Any:
	""" Edit a configuration property under a configuration group. """
	...

def enableAudit(*args: _Any) -> _Any:
	""" Enables Security Auditing and sets the auditEnabled field in audit.xml. """
	...

def enableAuditEncryption(*args: _Any) -> _Any:
	""" Enables audit encryption. """
	...

def enableAuditFilter(*args: _Any) -> _Any:
	""" Enables the Audit Specification. """
	...

def enableAuditSigning(*args: _Any) -> _Any:
	""" Enables audit signing. """
	...

def enableFips(*args: _Any) -> _Any:
	""" Enables and disables a specified FIPS security level. """
	...

def enableIntelligentManagement(*args: _Any) -> _Any:
	""" Command to enable Intelligent Management """
	...

def enableLMServiceEventPoint(*args: _Any) -> _Any:
	""" Use the "enableLMServiceEventPoint" command to enable a local mapping service event point, in order to generate service mapping events. """
	...

def enableOAuthTAI(*args: _Any) -> _Any:
	""" Enable OAuth TAI """
	...

def enablePasswordEncryption(*args: _Any) -> _Any:
	""" Generates and configures the key file and passwordUtil.properties file, both of which are required for AES password encryption. """
	...

def enableProvisioning(*args: _Any) -> _Any:
	""" Enable provisioning on a server. Some components will be started as they are needed. """
	...

def enableVerboseAudit(*args: _Any) -> _Any:
	""" Enables the verbose gathering of audit data. """
	...

def enableWritableKeyrings(*args: _Any) -> _Any:
	""" Modify keystore for writable SAF support.  This task is used during the migration process and will create additional writable keystore objects for the control region and servant region keyrings for SSL keystores. """
	...

def exchangeSigners(*args: _Any) -> _Any:
	""" Exchange Signer Certificates """
	...

def executeElasticityAction(*args: _Any) -> _Any:
	""" Command to execute a elasticity action """
	...

def executeHealthAction(*args: _Any) -> _Any:
	""" Command to execute a health action """
	...

def executeMiddlewareServerOperation(*args: _Any) -> _Any:
	""" Use this command to execute an operation on a middleware server """
	...

def exportAsset(*args: _Any) -> _Any:
	""" Export an asset which has been imported into the product configuration repository.  Only the asset file itself is exported.  No import options for the asset are exported. """
	...

def exportAuditCertToManagedKS(*args: _Any) -> _Any:
	""" Exports a personal certificate from a managed key to another managed key store. """
	...

def exportAuditCertificate(*args: _Any) -> _Any:
	""" Export a certificate to another KeyStore. """
	...

def exportBinding(*args: _Any) -> _Any:
	""" The exportBinding command exports a binding as an archive that can be copied onto a client environment or imported onto a server environment. """
	...

def exportCertToManagedKS(*args: _Any) -> _Any:
	""" Export a personal certificate to a managed keystore in the configuration. """
	...

def exportCertificate(*args: _Any) -> _Any:
	""" Export a certificate to another KeyStore. """
	...

def exportCompositeToDomain(*args: _Any) -> _Any:
	""" Exports composites under specified domain """
	...

def exportDeploymentManifest(*args: _Any) -> _Any:
	""" Export the deployment manifest from an EBA asset. """
	...

def exportLTPAKeys(*args: _Any) -> _Any:
	""" Exports Lightweight Third Party Authentication keys to a file. """
	...

def exportMiddlewareApp(*args: _Any) -> _Any:
	""" Use this command to export a middleware application to a directory. """
	...

def exportMiddlewareAppScript(*args: _Any) -> _Any:
	""" Use this command to export middleware application scripts to a directory. """
	...

def exportOAuthProps(*args: _Any) -> _Any:
	""" Get OAuth Configuration to edit """
	...

def exportPolicySet(*args: _Any) -> _Any:
	""" The exportPolicySet command exports a policy set as an archive that can be copied onto a client environment or imported onto a server environment. """
	...

def exportProxyProfile(*args: _Any) -> _Any:
	""" export the configuration of a wsprofile to a config archive. """
	...

def exportProxyServer(*args: _Any) -> _Any:
	""" export the configuration of a server to a config archive. """
	...

def exportSAMLSpMetadata(*args: _Any) -> _Any:
	""" This command exports the security configuration SAML TAI SP metadata to a file. """
	...

def exportSCDL(*args: _Any) -> _Any:
	""" Export the SCA SCDL """
	...

def exportServer(*args: _Any) -> _Any:
	""" export the configuration of a server to a config archive. """
	...

def exportTunnelTemplate(*args: _Any) -> _Any:
	""" Export a tunnel template and its children into a simple properties file. """
	...

def exportWSDLArtifacts(*args: _Any) -> _Any:
	""" Export WSDL and XSD documents for a specific Composition Unit """
	...

def exportWasprofile(*args: _Any) -> _Any:
	""" export the configuration of a wsprofile to a config archive. """
	...

def extractCertificate(*args: _Any) -> _Any:
	""" extract a signer certificate to a file. """
	...

def extractCertificateRequest(*args: _Any) -> _Any:
	""" Extract a certificate request to a file. """
	...

def extractConfigProperties(*args: _Any) -> _Any:
	""" Extracts configuration of the object specified by ConfigId or ConfigData parameter to a specified properies file. Either ConfigId or ConfigData parameter should be specified, but not both. ConfigId parameter should be in the form that is returned by "AdminConfig list configType". Example of ConfigId is cellName(cells/cellName|cell.xml#Cell_1). ConfigData parameter should be in the form of configType=value[:configType=value]*. Examples of configData are Deployment=appName or Node=nodeName:Server=serverName. """
	...

def extractRepositoryCheckpoint(*args: _Any) -> _Any:
	""" Extract the repository checkpoint specified by the "checkpointName" to the file specified by the "extractToFile". """
	...

def extractSignerCertificate(*args: _Any) -> _Any:
	""" Extract a signer certificate from a keystore. """
	...

def findOtherRAsToUpdate(*args: _Any) -> _Any:
	""" Find other Resource Adapters that are copies of the entered Resource Adapter.  Since an update will replace binary files, these copies of the Resource Adapter should be updated after the current Resource Adapter is updated. """
	...

def genAndReplaceCertificates(*args: _Any) -> _Any:
	""" Generates a new certificate with new specification options that replaces existing certificates as specified by the parameter configuration. """
	...

def generateKeyForKeySet(*args: _Any) -> _Any:
	""" Generate all the keys in a KeySet. """
	...

def generateKeyForKeySetGroup(*args: _Any) -> _Any:
	""" Generate new keys for all the keys within a keySet Group. """
	...

def generateSecConfigReport(*args: _Any) -> _Any:
	""" Generates the Security Configuration report. """
	...

def generateTemplates(*args: _Any) -> _Any:
	""" Generates new set of templates by combining WebSphere Application Server base product templates with feature pack and/or stack product templates """
	...

def getAccessIdFromServerId(*args: _Any) -> _Any:
	""" Returns the access ID for the registry server ID. """
	...

def getActiveSecuritySettings(*args: _Any) -> _Any:
	""" Gets the active security setting for global security or in a security domain. """
	...

def getAllCoreGroupNames(*args: _Any) -> _Any:
	""" Get the names of all core groups """
	...

def getAuditCertificate(*args: _Any) -> _Any:
	""" Get information about a personal certificate. """
	...

def getAuditEmitter(*args: _Any) -> _Any:
	""" Returns an audit emitter implementation object. """
	...

def getAuditEmitterFilters(*args: _Any) -> _Any:
	""" Returns a list of defined filters for the supplied emitter in shortened format. """
	...

def getAuditEncryptionConfig(*args: _Any) -> _Any:
	""" Returns the audit record encryption configuration. """
	...

def getAuditEventFactory(*args: _Any) -> _Any:
	""" Returns the object of the supplied event factory. """
	...

def getAuditEventFactoryClass(*args: _Any) -> _Any:
	""" Returns the class name for the supplied event factory. """
	...

def getAuditEventFactoryFilters(*args: _Any) -> _Any:
	""" Returns a list of defined filters for the supplied event factory in shortened format. """
	...

def getAuditEventFactoryName(*args: _Any) -> _Any:
	""" Returns the unique name for the supplied event factory. """
	...

def getAuditEventFactoryProvider(*args: _Any) -> _Any:
	""" Returns the configured audit service provider for the supplied event factory. """
	...

def getAuditFilter(*args: _Any) -> _Any:
	""" Returns an audit specification entry in the audit.xml that matches the reference Id. """
	...

def getAuditKeyStoreInfo(*args: _Any) -> _Any:
	""" Shows information about a particular key store. """
	...

def getAuditNotification(*args: _Any) -> _Any:
	""" Returns an audit notification. """
	...

def getAuditNotificationMonitor(*args: _Any) -> _Any:
	""" Returns the audit notification monitor specified by the reference id. """
	...

def getAuditNotificationName(*args: _Any) -> _Any:
	""" Returns the name of the configured audit notification. """
	...

def getAuditNotificationRef(*args: _Any) -> _Any:
	""" Returns the reference id of the configured audit notification. """
	...

def getAuditOutcomes(*args: _Any) -> _Any:
	""" Returns the audit outcomes defined for an event. """
	...

def getAuditPolicy(*args: _Any) -> _Any:
	""" Returns the audit policy attributes. """
	...

def getAuditSigningConfig(*args: _Any) -> _Any:
	""" Returns the audit record signing configuration. """
	...

def getAuditSystemFailureAction(*args: _Any) -> _Any:
	""" Returns the audit system failure policy. """
	...

def getAuditorId(*args: _Any) -> _Any:
	""" Gets the auditor identity defined in the audit.xml file. """
	...

def getAuthDataEntry(*args: _Any) -> _Any:
	""" Return information about an authentication data entry """
	...

def getAuthzConfigInfo(*args: _Any) -> _Any:
	""" Return information about an external JAAC authorization provider. """
	...

def getAutoCheckpointDepth(*args: _Any) -> _Any:
	""" Get the depth of the automatic checkpoints """
	...

def getAutoCheckpointEnabled(*args: _Any) -> _Any:
	""" Get the automatic checkpoints enabled attribute value """
	...

def getAvailableSDKsOnNode(*args: _Any) -> _Any:
	""" Returns a list of names for the SDKs on a given node. """
	...

def getBLAStatus(*args: _Any) -> _Any:
	""" Determine whether a business-level application or composition unit is running or stopped. """
	...

def getBinaryFileLocation(*args: _Any) -> _Any:
	""" Returns the file location of the Binary audit log. """
	...

def getBinaryFileSize(*args: _Any) -> _Any:
	""" Returns the file size of the Binary audit log. """
	...

def getBinding(*args: _Any) -> _Any:
	""" The getBinding command returns the binding configuration for a specified policy type and scope. """
	...

def getCAClient(*args: _Any) -> _Any:
	""" Gets information about a certificate authority (CA) client configurator object. """
	...

def getCSIInboundInfo(*args: _Any) -> _Any:
	""" Returns the CSI inbound information for global security or in a security domain. """
	...

def getCSIOutboundInfo(*args: _Any) -> _Any:
	""" Returns the CSI outbound information for global security or in a security domain. """
	...

def getCertificate(*args: _Any) -> _Any:
	""" Get information about a personal certificate. """
	...

def getCertificateChain(*args: _Any) -> _Any:
	""" Gets information about each certificate in a certificate chain. """
	...

def getCertificateRequest(*args: _Any) -> _Any:
	""" Get information about a certificate request """
	...

def getCheckpointLocation(*args: _Any) -> _Any:
	""" Get the directory path where the checkpoints are stored """
	...

def getClientDynamicPolicyControl(*args: _Any) -> _Any:
	""" The getClientDynamicPolicyControl command returns the WSPolicy client acquisition information for a specified application or resource. """
	...

def getConfigRepositoryLocation(*args: _Any) -> _Any:
	""" Get the directory path where the configuration repository is stored """
	...

def getContexts(*args: _Any) -> _Any:
	""" getContextDesc """
	...

def getCoreGroupNameForServer(*args: _Any) -> _Any:
	""" Get the name of the core group the server is a member of. """
	...

def getCurrentWizardSettings(*args: _Any) -> _Any:
	""" Gets current security wizard settings from the workspace. """
	...

def getDefaultBindings(*args: _Any) -> _Any:
	""" The getDefaultBindings command returns the default binding names for a specified domain or server. """
	...

def getDefaultContextService(*args: _Any) -> _Any:
	""" Get the JNDI name that is bound to java:comp/DefaultContextService. """
	...

def getDefaultCoreGroupName(*args: _Any) -> _Any:
	""" Get the name of the default core group """
	...

def getDefaultDataSource(*args: _Any) -> _Any:
	""" Get the JNDI name that is bound to java:comp/DefaultDataSource. """
	...

def getDefaultJMSConnectionFactory(*args: _Any) -> _Any:
	""" Get the JNDI name that is bound to java:comp/DefaultJMSConnectionFactory. """
	...

def getDefaultManagedExecutor(*args: _Any) -> _Any:
	""" Get the JNDI name that is bound to java:comp/DefaultManagedExecutorService. """
	...

def getDefaultManagedScheduledExecutor(*args: _Any) -> _Any:
	""" Get the JNDI name that is bound to java:comp/DefaultManagedScheduledExecutorService. """
	...

def getDefaultManagedThreadFactory(*args: _Any) -> _Any:
	""" Get the JNDI name that is bound to java:comp/DefaultManagedThreadFactory. """
	...

def getDescriptiveProp(*args: _Any) -> _Any:
	""" Get information about a descriptive property under an object. """
	...

def getDistributedCacheProperty(*args: _Any) -> _Any:
	""" queryDistrbitedConfigCmdDesc """
	...

def getDmgrProperties(*args: _Any) -> _Any:
	""" Returns the properties of the deployment manager """
	...

def getDynamicClusterIsolationProperties(*args: _Any) -> _Any:
	""" Display Dynamic Cluster isolation properties """
	...

def getDynamicClusterMaxInstances(*args: _Any) -> _Any:
	""" Get dynamic cluster maximum number of cluster instances """
	...

def getDynamicClusterMaxNodes(*args: _Any) -> _Any:
	""" Get dynamic cluster maximum number of cluster nodes """
	...

def getDynamicClusterMembers(*args: _Any) -> _Any:
	""" Get members of specified dynamic cluster and node name.  If node name is not specified, all members of the dynamic cluster are returned. """
	...

def getDynamicClusterMembershipPolicy(*args: _Any) -> _Any:
	""" Get dynamic cluster membership policy """
	...

def getDynamicClusterMinInstances(*args: _Any) -> _Any:
	""" Get dynamic cluster minimum number of cluster instances """
	...

def getDynamicClusterMinNodes(*args: _Any) -> _Any:
	""" Get dynamic cluster minimum number of cluster nodes """
	...

def getDynamicClusterOperationalMode(*args: _Any) -> _Any:
	""" Get dynamic cluster operational mode """
	...

def getDynamicClusterServerIndexTemplateId(*args: _Any) -> _Any:
	""" Get the configuration ID of the specified dynamic cluster's ServerIndex template object. """
	...

def getDynamicClusterServerType(*args: _Any) -> _Any:
	""" Get dynamic cluster server type """
	...

def getDynamicClusterVerticalInstances(*args: _Any) -> _Any:
	""" Get dynamic cluster vertical stacking of instances on node """
	...

def getDynamicSSLConfigSelection(*args: _Any) -> _Any:
	""" Get information about a Dynamic SSL configuration selection. """
	...

def getEditionState(*args: _Any) -> _Any:
	""" Provides the state of an application edition. """
	...

def getEmailList(*args: _Any) -> _Any:
	""" Returns the notification email list for the configured audit notification. """
	...

def getEmitterClass(*args: _Any) -> _Any:
	""" Returns the class name associated with the supplied emitter reference. """
	...

def getEmitterUniqueId(*args: _Any) -> _Any:
	""" Returns the unique ID associated with the supplied emitter reference. """
	...

def getEncryptionKeyStore(*args: _Any) -> _Any:
	""" Returns the keystore containing the certificate used to encrypt the audit records. """
	...

def getEventFormatterClass(*args: _Any) -> _Any:
	""" Returns the class name of the event formatter associated with the audit service provider reference. """
	...

def getFipsInfo(*args: _Any) -> _Any:
	""" Returns information about the FIPS settings in the current WebSphere configuration.  It will print out whether the FIPS is enabled or not and if it is, then what level FIPS setting is enabled. If suite B is enabled, the level of suite B is also returned. """
	...

def getGroup(*args: _Any) -> _Any:
	""" Retrieves the attributes of a group. """
	...

def getIdMgrDefaultRealm(*args: _Any) -> _Any:
	""" Returns the name of the default realm. """
	...

def getIdMgrEntityTypeSchema(*args: _Any) -> _Any:
	""" Retrieves the schema of an entity type. If repository ID is not specified then it returns the default entity type schema supported by virtual member manager. If entity type names are not specified then it retrieves the entity type schema for all the entity types. """
	...

def getIdMgrLDAPAttrCache(*args: _Any) -> _Any:
	""" Returns the LDAP attribute cache configuration. """
	...

def getIdMgrLDAPContextPool(*args: _Any) -> _Any:
	""" Returns LDAP context pool configuration. """
	...

def getIdMgrLDAPEntityType(*args: _Any) -> _Any:
	""" Returns the LDAP entity type configuration data for the specified entity type in the LDAP repository. """
	...

def getIdMgrLDAPEntityTypeRDNAttr(*args: _Any) -> _Any:
	""" Returns the RDN attributes configuration of an LDAP entity type configuration. """
	...

def getIdMgrLDAPGroupConfig(*args: _Any) -> _Any:
	""" Returns the LDAP group configuration parameters. """
	...

def getIdMgrLDAPGroupDynamicMemberAttrs(*args: _Any) -> _Any:
	""" Returns the dynamic member attribute configuration from the LDAP group configuration. """
	...

def getIdMgrLDAPGroupMemberAttrs(*args: _Any) -> _Any:
	""" Returns the member attribute configuration from the LDAP group configuration. """
	...

def getIdMgrLDAPSearchResultCache(*args: _Any) -> _Any:
	""" Returns the LDAP search result cache configuration. """
	...

def getIdMgrLDAPServer(*args: _Any) -> _Any:
	""" Returns all the configured LDAP servers and their configurations. """
	...

def getIdMgrPropertySchema(*args: _Any) -> _Any:
	""" Retrieves the property schema of an entity type. If repository ID is not specified then it returns the default property schema supported by virtual member manager. If propertyNames is not specified it returns schema of all the properties. If entity type is not specified then it retrieves the property schema for all entity types. If propertyNames is specified then entityTypeName must be specified. """
	...

def getIdMgrRealm(*args: _Any) -> _Any:
	""" Returns the specified realm configuration. """
	...

def getIdMgrRepositoriesForRealm(*args: _Any) -> _Any:
	""" Returns repository specific details for the repositories configuration for the specified realm. """
	...

def getIdMgrRepository(*args: _Any) -> _Any:
	""" Returns the configuration of the specified repository. """
	...

def getIdMgrSupportedDataTypes(*args: _Any) -> _Any:
	""" Retrieves the supported data types. If repository ID is not specified then it returns the default data types supported by virtual member manager. """
	...

def getIdMgrSupportedEntityType(*args: _Any) -> _Any:
	""" Returns the configuration of the specified supported entity type. """
	...

def getInheritedSSLConfig(*args: _Any) -> _Any:
	""" Returns a string containing the alias of the SSL Configuration and the certificate alias for the specified scope. """
	...

def getJAASLoginEntryInfo(*args: _Any) -> _Any:
	""" Get information about a JAAS login entry. """
	...

def getJVMMode(*args: _Any) -> _Any:
	""" Get the current JVM mode. The command will return either 31-bit or 64-bit. """
	...

def getJaspiInfo(*args: _Any) -> _Any:
	""" Display information about the Jaspi configuration. """
	...

def getJavaHome(*args: _Any) -> _Any:
	""" Get the Java Home path. """
	...

def getJobTargetHistory(*args: _Any) -> _Any:
	""" This command is used to get the job target history for a job. """
	...

def getJobTargetStatus(*args: _Any) -> _Any:
	""" This command is used to get the latest job target status for a job. """
	...

def getJobTargets(*args: _Any) -> _Any:
	""" This command is used to get targets for a job.  The targets for the job may have been unregistered, or deleted. """
	...

def getJobTypeMetadata(*args: _Any) -> _Any:
	""" This command is used to get the metadata associated with a jobType. """
	...

def getJobTypes(*args: _Any) -> _Any:
	""" This command is used to get the supported job types for a managed node. """
	...

def getKeyManager(*args: _Any) -> _Any:
	""" Get information about a key manager. """
	...

def getKeyReference(*args: _Any) -> _Any:
	""" Get information about a Key Reference in a particular keySet. """
	...

def getKeySet(*args: _Any) -> _Any:
	""" Get information about a key set. """
	...

def getKeySetGroup(*args: _Any) -> _Any:
	""" Get information about a key set group. """
	...

def getKeyStoreInfo(*args: _Any) -> _Any:
	""" Returns information about a particular keystore. """
	...

def getLTPATimeout(*args: _Any) -> _Any:
	""" Return the LTPA authentication mechanism timeout from global security or a security domain. """
	...

def getManagedNodeConnectorProperties(*args: _Any) -> _Any:
	""" Get connector properties for the managed node """
	...

def getManagedNodeGroupInfo(*args: _Any) -> _Any:
	""" Information regarding a group of managed nodes. (deprecated) """
	...

def getManagedNodeGroupMembers(*args: _Any) -> _Any:
	""" This command is used to list members of a group of managed nodes. (deprecated) """
	...

def getManagedNodeKeys(*args: _Any) -> _Any:
	""" Get properties keys associated with a specific managed node. (deprecated) """
	...

def getManagedNodeProperties(*args: _Any) -> _Any:
	""" Get properties associated with a specific managed node. (deprecated) """
	...

def getManagedResourceProperties(*args: _Any) -> _Any:
	""" Get properties associated with a specific managed resource. """
	...

def getManagedResourcePropertyKeys(*args: _Any) -> _Any:
	""" Get property keys associated with an specific managed resource. """
	...

def getManagedResourceTypes(*args: _Any) -> _Any:
	""" Retrieves managed resource types. """
	...

def getManagementScope(*args: _Any) -> _Any:
	""" Get information about a management scope. """
	...

def getMaxNumBinaryLogs(*args: _Any) -> _Any:
	""" Returns the configured maximum number of Binary audit logs. """
	...

def getMembersOfGroup(*args: _Any) -> _Any:
	""" Retrieves the members of a group. """
	...

def getMembershipOfGroup(*args: _Any) -> _Any:
	""" Retrieves the groups in which a group is a member. """
	...

def getMembershipOfUser(*args: _Any) -> _Any:
	""" Get the groups in which a PersonAccount is a member. """
	...

def getMetadataProperties(*args: _Any) -> _Any:
	""" Returns all managed object metadata properties for a given node. """
	...

def getMetadataProperty(*args: _Any) -> _Any:
	""" Returns the specified managed object metadata property for agiven node. """
	...

def getMiddlewareServerType(*args: _Any) -> _Any:
	""" Use this command to show the server type of a middleware server """
	...

def getMigrationOptions(*args: _Any) -> _Any:
	""" Returns the default migration scan options used by the createMigrationReport command """
	...

def getMigrationReport(*args: _Any) -> _Any:
	""" Returns the absolute path for an application's Liberty migration report """
	...

def getMigrationSummary(*args: _Any) -> _Any:
	""" Returns a summary of a Liberty migration report for an application """
	...

def getNamedTCPEndPoint(*args: _Any) -> _Any:
	""" Returns the port associated with the specified bridge interface.  This is the port specified on the TCP inbound channel of transport channel chain for the specified bridge interface. """
	...

def getNewRAObjectProperties(*args: _Any) -> _Any:
	""" Returns a string containing all of the property values and step inputs for the updateRAR command. """
	...

def getNodeBaseProductVersion(*args: _Any) -> _Any:
	""" Returns the base version for a node, for example, "6.0.0.0". """
	...

def getNodeDefaultSDK(*args: _Any) -> _Any:
	""" Query the node's default SDK name and location """
	...

def getNodeMajorVersion(*args: _Any) -> _Any:
	""" Returns the major version for a node, for example, "6" for v6.0.0.0. """
	...

def getNodeMinorVersion(*args: _Any) -> _Any:
	""" Returns the minor version for a node, for example, "0.0.0" for v6.0.0.0. """
	...

def getNodePlatformOS(*args: _Any) -> _Any:
	""" Returns the operating system platform for a given node. """
	...

def getNodeSysplexName(*args: _Any) -> _Any:
	""" Returns the operating system platform for a given node.  This valueapplies only to nodes running on the z/OS operating system. """
	...

def getOSGiApplicationDeployedObject(*args: _Any) -> _Any:
	""" Returns the deployedObject that represents the configuration of the OSGi application given the name of its composition unit. """
	...

def getOverallJobStatus(*args: _Any) -> _Any:
	""" This command is used to get overall status of a job. """
	...

def getPolicySet(*args: _Any) -> _Any:
	""" The getPolicySet command returns general attributes, such as description and default indicator, for the specified policy set. """
	...

def getPolicySetAttachments(*args: _Any) -> _Any:
	""" The getPolicySetAttachments command lists the properties for all attachments configured for a specified application or for the trust service. """
	...

def getPolicyType(*args: _Any) -> _Any:
	""" The getPolicyType command returns the attributes for a specified policy. """
	...

def getPolicyTypeAttribute(*args: _Any) -> _Any:
	""" The getPolicyTypeAttribute command returns the value for the specified policy attribute. """
	...

def getPreferences(*args: _Any) -> _Any:
	""" Command to get user preferences """
	...

def getProfileKey(*args: _Any) -> _Any:
	""" Get the profile key """
	...

def getProviderPolicySharingInfo(*args: _Any) -> _Any:
	""" The getProviderPolicySharingInfo command returns the WSPolicy provider sharing information for a specified application or resource. """
	...

def getRSATokenAuthorization(*args: _Any) -> _Any:
	""" Returns information in the admin RSA token authorization mechanism object. """
	...

def getRequiredBindingVersion(*args: _Any) -> _Any:
	""" The getRequiredBindingVersion command returns the binding version that is required for a specified asset. """
	...

def getRuntimeRegistrationProperties(*args: _Any) -> _Any:
	""" Get certain runtime properties pertaining to a device and its registered job manager """
	...

def getSDKPropertiesOnNode(*args: _Any) -> _Any:
	""" Returns properties for the SDKs. If the SDK name is not given, all properties for all avaiable SDKs are returned.  If the SDK attributes are specified, only properties for given SDK attributes are returned. """
	...

def getSDKVersion(*args: _Any) -> _Any:
	""" Query the SDK version number in use """
	...

def getSSLConfig(*args: _Any) -> _Any:
	""" Get information about a particular SSL configuration. """
	...

def getSSLConfigGroup(*args: _Any) -> _Any:
	""" Get information about a SSL configuration group. """
	...

def getSSLConfigProperties(*args: _Any) -> _Any:
	""" Get SSL Configuration Properties """
	...

def getSecurityDomainForResource(*args: _Any) -> _Any:
	""" Returns the security domain that a particular scope belongs to. """
	...

def getSendEmail(*args: _Any) -> _Any:
	""" Returns the state of the sendEmail audit notification. """
	...

def getServerSDK(*args: _Any) -> _Any:
	""" Query the server's SDK name and location """
	...

def getServerSecurityLevel(*args: _Any) -> _Any:
	""" Get the current security level of the secure proxy server. """
	...

def getServerType(*args: _Any) -> _Any:
	""" returns the server type of the specified server. """
	...

def getSignerCertificate(*args: _Any) -> _Any:
	""" Get information about a signer Certificate. """
	...

def getSingleSignon(*args: _Any) -> _Any:
	""" Returns information about the single signon settings for global security. """
	...

def getSupportedAuditEvents(*args: _Any) -> _Any:
	""" Returns all supported audit events. """
	...

def getSupportedAuditOutcomes(*args: _Any) -> _Any:
	""" Returns all supported audit outcomes. """
	...

def getTADataCollectionSummary(*args: _Any) -> _Any:
	""" This command returns a summary of the Transformation Advisor data collection status. """
	...

# --------------------------------------------------------------------------
@_overload
def getTCPEndPoint(options: _Literal['-interactive'], /) -> _Any:
    ...

@_overload
def getTCPEndPoint(target_object: ConfigurationObjectName, /) -> ConfigurationObjectName:
    ...

@_overload
def getTCPEndPoint(target_object: ConfigurationObjectName, options: _Union[str, _List[str]], /) -> ConfigurationObjectName:
    ...

def getTCPEndPoint(target_object: ConfigurationObjectName, options: _Union[str, _List[str]], /) -> ConfigurationObjectName: # type: ignore[misc]
    """Get the NamedEndPoint associated with either a TCPInboundChannel, or a chain that contains a TCPInboundChannel.

    - If `target_object` is set to a string with value `"-interactive"`, the endpoint will 
        be retrieved in _interactive mode_.

    Args:
        target_object (ConfigurationObjectName | _Literal['-interactive']): The TCPInboundChannel, or containing chain, instance that is associated with a NamedEndPoint. 

    Returns:
        ConfigurationObjectName: The object name of an existing named end point that is associated with the TCP inbound channel instance or a channel chain.
    
    Example:
        ```pycon
        >>> target = 'TCP_1(cells/mybuildCell01/nodes/mybuildCellManager01/servers/dmgr|server.xml#TCPInboundChannel_1)'
        >>> AdminTask.getTCPEndPoint(target)
        ```
    """
    ...
# --------------------------------------------------------------------------

def getTargetGroupInfo(*args: _Any) -> _Any:
	""" Information regarding a group of Targets. """
	...

def getTargetGroupMembers(*args: _Any) -> _Any:
	""" This command is used to list members of a target group. """
	...

def getTargetKeys(*args: _Any) -> _Any:
	""" Get properties keys associated with a specific Target. """
	...

def getTargetProperties(*args: _Any) -> _Any:
	""" Get properties associated with a specific Target. """
	...

def getTrustAssociationInfo(*args: _Any) -> _Any:
	""" Get information about a trust association. """
	...

def getTrustManager(*args: _Any) -> _Any:
	""" Get information about a trust manager. """
	...

def getUDPEndPoint(*args: _Any) -> _Any:
	""" Get the NamedEndPoint endpoint that is associated with either a UDPInboundChannel, or a chain that contains a UDPInboundChannel """
	...

def getUnusedSDKsOnNode(*args: _Any) -> _Any:
	""" Query unused SDKs on the node """
	...

def getUser(*args: _Any) -> _Any:
	""" Retrieves the attributes of a PersonAccount. """
	...

def getUserRegistryInfo(*args: _Any) -> _Any:
	""" Returns information about a user registry from the administrative security configuration or an application security domain. """
	...

def getWSCertExpMonitor(*args: _Any) -> _Any:
	""" Get information about a certificate expiration monitor. """
	...

def getWSN_SIBWSInboundPort(*args: _Any) -> _Any:
    """ Retrieve one of the service integration bus inbound ports from a WS-Notification service point. """
    ...

def getWSN_SIBWSInboundService(*args: _Any) -> _Any:
    """ Retrieve one of the service integration bus inbound services from a WS-Notification service. """
    ...

def getWSNotifier(*args: _Any) -> _Any:
	""" Get information about a notifier. """
	...

def getWSSchedule(*args: _Any) -> _Any:
	""" Get schedule information. """
	...

def getWebService(*args: _Any) -> _Any:
	""" Gets the attributes for a Web service in an enterprise application. """
	...

def healthRestartAction(*args: _Any) -> _Any:
	""" restarts the sick server """
	...

# --------------------------------------------------------------------------
def help(search_query: str = "", /) -> str:
    """The number of admin commands varies and depends on your WebSphere
    install. Use the following help commands to obtain a list of supported
    commands and their parameters:

    - `AdminTask.help("-commands")`                  list all the admin commands
    - `AdminTask.help("-commands <pattern>")`        list admin commands matching with wildcard "pattern"
    - `AdminTask.help("-commandGroups")`             list all the admin command groups
    - `AdminTask.help("-commandGroups <pattern>")`   list admin command groups matching with wildcard "pattern"
    - `AdminTask.help("commandName")`                display detailed information for the specified command
    - `AdminTask.help("commandName stepName")`       display detailed information for the specified step belonging to the specified command
    - `AdminTask.help("commandGroupName")`           display detailed information for the specified command group


    Args:
        search_query (str, optional): Pass a query to filter the desired results. Defaults to "".

    Returns:
        str: The detailed help string
    
    Example:
        ```pycon
        >>> print (AdminTask.help("createTCPEndPoint"))
        WASX8006I: Detailed help for command: createTCPEndPoint
        Description: Create a new NamedEndPoint that can be associated with a TCPInboundChannel
        [...]
        ```
    """
    ...
# --------------------------------------------------------------------------

def importApplicationsFromWasprofile(*args: _Any) -> _Any:
	""" Import the applications from a configuration archive file to a sepcified application server target. """
	...

def importAsset(*args: _Any) -> _Any:
	""" Import an application file into the product configuration repository as an asset. """
	...

def importAuditCertFromManagedKS(*args: _Any) -> _Any:
	""" Imports a personal certificate from another managed key store. """
	...

def importAuditCertificate(*args: _Any) -> _Any:
	""" Import a Certificate from another keyStore to this KeyStore. """
	...

def importBinding(*args: _Any) -> _Any:
	""" The importBinding command imports a binding from a compressed archive onto a server environment. """
	...

def importCertFromManagedKS(*args: _Any) -> _Any:
	""" Import a personal certificate from managed keystore in the configuration. """
	...

def importCertificate(*args: _Any) -> _Any:
	""" port a Certificate from another keystore to this keystore. """
	...

def importDeploymentManifest(*args: _Any) -> _Any:
	""" Import the deployment manifest into the EBA asset. If the deployment manifest is resolved successfully, it will replace the existing deployment manifest in the asset. """
	...

def importEncryptionCertificate(*args: _Any) -> _Any:
	""" Import a Certificate from another keyStore to this KeyStore. """
	...

def importLTPAKeys(*args: _Any) -> _Any:
	""" Imports Lightweight Third Party Authentication keys into the configuration. """
	...

def importOAuthProps(*args: _Any) -> _Any:
	""" Import OAuth Configuration After Export """
	...

def importPolicySet(*args: _Any) -> _Any:
	""" The importPolicySet command imports a policy set from a compressed archive onto a server environment. """
	...

def importProxyProfile(*args: _Any) -> _Any:
	""" Import a Secure Proxy Profile into this cell. """
	...

def importProxyServer(*args: _Any) -> _Any:
	""" Import a Secure Proxy Server into a given Secure Proxy node. """
	...

def importSAMLIdpMetadata(*args: _Any) -> _Any:
	""" This command imports SAML IdP metadata to the security configuration SAML TAI. """
	...

def importServer(*args: _Any) -> _Any:
	""" Import a server configuration from a configuration archive. This command creates a new server based on the server configuration defined in the archive. """
	...

def importTunnelTemplate(*args: _Any) -> _Any:
	""" Import a tunnel template and its children into the cell-scoped config. """
	...

def importWasprofile(*args: _Any) -> _Any:
	""" Import the configuration of a wasprofile profile from a configuration archive. This command overwrites the configuration of the current wasprofile configuration. """
	...

def inspectServiceMapLibrary(*args: _Any) -> _Any:
	""" Use the "inspectServiceMapLibrary" command to display details about the service maps within a service map library. """
	...

def installPHPApp(*args: _Any) -> _Any:
	""" Use this command to install a PHP application. """
	...

def installResourceAdapter(*args: _Any) -> _Any:
	""" Install a J2C resource adapter """
	...

def installServiceMap(*args: _Any) -> _Any:
	""" Use the "installServiceMap" command to install a service map in a service map library. """
	...

def installWasCEApp(*args: _Any) -> _Any:
	""" Use this command to install a WAS CE application. """
	...

def isAdminLockedOut(*args: _Any) -> _Any:
	""" Checks to make sure that at least one admin user in the admin-authz.xml file exists in the input user registry. """
	...

def isAppSecurityEnabled(*args: _Any) -> _Any:
	""" Returns the current Application Security setting of true or false. """
	...

def isAuditEnabled(*args: _Any) -> _Any:
	""" Returns the state of Security Auditing. """
	...

def isAuditEncryptionEnabled(*args: _Any) -> _Any:
	""" Returns the state of audit encryption. """
	...

def isAuditFilterEnabled(*args: _Any) -> _Any:
	""" Determination of enablement state of an Audit Specification. """
	...

def isAuditNotificationEnabled(*args: _Any) -> _Any:
	""" Returns the enabled state of the audit notification policy. """
	...

def isAuditSigningEnabled(*args: _Any) -> _Any:
	""" Returns the state of audit signing. """
	...

def isEditionExists(*args: _Any) -> _Any:
	""" Use this command to check if the specified edition exists for the particular application. """
	...

def isEventEnabled(*args: _Any) -> _Any:
	""" Returns a Boolean indicating if the event has at least one audit outcome for which it has been enabled. """
	...

def isFederated(*args: _Any) -> _Any:
	""" Check if the server is a standalone server or the node of the given server is federated with a deployment manager. Returns "true" if the node of the server is federated, "false" otherwise. """
	...

def isGlobalSecurityEnabled(*args: _Any) -> _Any:
	""" Returns the current administrative security setting of true or false. """
	...

def isIdMgrUseGlobalSchemaForModel(*args: _Any) -> _Any:
	""" Returns a boolean to indicate whether the global schema option is enabled for the data model in a multiple security domain environment. """
	...

def isInheritDefaultsForDestination(*args: _Any) -> _Any:
	""" The command will return "true" if the destination specified inherits the default security permissions. """
	...

def isInheritReceiverForTopic(*args: _Any) -> _Any:
	""" Shows the inherit receiver defaults for a topic in a given topic space.  Returns "true" if the topic inherits from receiver default values. """
	...

def isInheritSenderForTopic(*args: _Any) -> _Any:
	""" Shows the inherit sender defaults for a topic for a specified topic space.  Returns "true" if the topic inherits from sender default values. """
	...

def isJACCEnabled(*args: _Any) -> _Any:
	""" Checks if the current run time is JACC enabled in the global security domain. """
	...

def isNodeZOS(*args: _Any) -> _Any:
	""" Determines whether or not a given node is a z/OS node. Returns "true" if node operating system is Z/OS, "false" otherwise. """
	...

def isPollingJobManager(*args: _Any) -> _Any:
	""" Query whether a managed node is periodically polling a JobManager """
	...

def isSAFVersionValidForIdentityMapping(*args: _Any) -> _Any:
	""" Returns a Boolean indicating if the version of the SAF product supports distributed identity mapping. """
	...

def isSendEmailEnabled(*args: _Any) -> _Any:
	""" Returns the enabled state of sending audit notification emails. """
	...

def isSingleSecurityDomain(*args: _Any) -> _Any:
	""" Checks if the current run time is a single security domain. """
	...

def isVerboseAuditEnabled(*args: _Any) -> _Any:
	""" Returns the state of verbose gathering of audit data. """
	...

def ldapSearch(*args: _Any) -> _Any:
	""" Performs ldapsearch according to search criteria from input parameter """
	...

def listAdminObjectInterfaces(*args: _Any) -> _Any:
	""" List all of the defined administrative object interfaces on the specified J2C resource adapter. """
	...

def listAllDestinationsWithRoles(*args: _Any) -> _Any:
	""" Lists all destinations which have roles defined on them. """
	...

def listAllForeignBusesWithRoles(*args: _Any) -> _Any:
	""" Lists all foreign buses which have roles defined on them for the specified bus. """
	...

def listAllRolesForGroup(*args: _Any) -> _Any:
	""" Lists all the roles defined for a specified group. """
	...

def listAllRolesForUser(*args: _Any) -> _Any:
	""" Lists all the roles defined for a specified user. """
	...

def listAllSIBBootstrapMembers(*args: _Any) -> _Any:
	""" Lists all the servers or clusters that can be used for bootstrap into the specified bus. """
	...

def listAllTopicsWithRoles(*args: _Any) -> _Any:
	""" Lists all the topics with roles defined for the specified topic space. """
	...

def listApplicationPorts(*args: _Any) -> _Any:
	""" Displays a list of ports that is used to access the specified application, including the node name, server name, named endpoint, and host and port values. """
	...

def listAssets(*args: _Any) -> _Any:
	""" List assets which have been imported into the product configuration repository. """
	...

def listAssetsAttachedToPolicySet(*args: _Any) -> _Any:
	""" The listAssetsAttachedToPolicySet command lists the assets to which a specific policy set is attached. """
	...

def listAttachmentsForPolicySet(*args: _Any) -> _Any:
	""" The listAttachmentsForPolicySet command lists the applications to which a specific policy set is attached. """
	...

def listAuditAuthorizationGroupsForGroupID(*args: _Any) -> _Any:
	""" list all the AuthorizationGroups that a given group has access to """
	...

def listAuditAuthorizationGroupsForUserID(*args: _Any) -> _Any:
	""" list all the AuthorizationGroups that a given user has access to. """
	...

def listAuditEmitters(*args: _Any) -> _Any:
	""" Lists all the audit emitter implementation objects. """
	...

def listAuditEncryptionKeyStores(*args: _Any) -> _Any:
	""" Lists the audit record encryption keystores. """
	...

def listAuditEventFactories(*args: _Any) -> _Any:
	""" Returns a list of the defined audit event factory implementations. """
	...

def listAuditFilters(*args: _Any) -> _Any:
	""" Retrieves a list of all the audit specifications defined in the audit.xml. """
	...

def listAuditFiltersByEvent(*args: _Any) -> _Any:
	""" Returns a list of event and outcome types of the defined Audit Filters. """
	...

def listAuditFiltersByRef(*args: _Any) -> _Any:
	""" Returns the references to the defined Audit Filters. """
	...

def listAuditGroupIDsOfAuthorizationGroup(*args: _Any) -> _Any:
	""" list all the group IDs in an AuthorizationGroups """
	...

def listAuditKeyStores(*args: _Any) -> _Any:
	""" Lists Audit keystores """
	...

def listAuditNotificationMonitors(*args: _Any) -> _Any:
	""" Lists the audit notification monitors. """
	...

def listAuditNotifications(*args: _Any) -> _Any:
	""" Lists the audit notifications. """
	...

def listAuditResourcesForGroupID(*args: _Any) -> _Any:
	""" List all the objects that a given group has access to. """
	...

def listAuditResourcesForUserID(*args: _Any) -> _Any:
	""" List all the objects that a given user has access to. """
	...

def listAuditUserIDsOfAuthorizationGroup(*args: _Any) -> _Any:
	""" list all the users IDs in an AuthorizationGroups """
	...

def listAuthDataEntries(*args: _Any) -> _Any:
	""" List authentication data entries in the administrative security configuration or a in a security domain. """
	...

def listAuthorizationGroups(*args: _Any) -> _Any:
	""" List existing Authorization Groups. """
	...

def listAuthorizationGroupsForGroupID(*args: _Any) -> _Any:
	""" list all the AuthorizationGroups that a given group has access to """
	...

def listAuthorizationGroupsForUserID(*args: _Any) -> _Any:
	""" list all the AuthorizationGroups that a given user has access to. """
	...

def listAuthorizationGroupsOfResource(*args: _Any) -> _Any:
	""" Get the authorization groups of a given Resource. """
	...

def listAvailableOSGiExtensions(*args: _Any) -> _Any:
	""" Shows the possible extensions available to be attached to the composition unit. """
	...

def listBLAs(*args: _Any) -> _Any:
	""" List business-level applications in the cell. """
	...

def listCAClients(*args: _Any) -> _Any:
	""" Lists certificate authority (CA) client configurator objects. """
	...

def listCertAliases(*args: _Any) -> _Any:
	""" Lists the certificate aliases. """
	...

def listCertStatusForSecurityStandard(*args: _Any) -> _Any:
	""" Returns all the certificate used by SSL configuraiton and plugins. States if they comply with the requested security level. """
	...

def listCertificateRequests(*args: _Any) -> _Any:
	""" The list of certificate request in a keystore. """
	...

def listChainTemplates(*args: _Any) -> _Any:
	""" Displays a list of templates that can be used to create chains in this configuration. All templates have a certain type of transport channel as the last transport channel in the chain. """
	...

def listChains(acceptor_filter: ConfigurationObjectName, endpoint_filter: str, /) -> MultilineList[ConfigurationObjectName]:
	""" List all chains configured under a particular instance of TransportChannelService. 
    
	Args:
        acceptor_filter (ConfigurationObjectName): Chains returned by this method should all have a transport channel instance of the specified type as the last transport channel in the chain.
        endpoint_filter (str): Chains returned by this method should all have a TCPInboundChannel using an end point with the specified name.

    Returns:
        chains (ConfigurationObjectName): _List of all the chains satisfying the filters specified by `endpoint_filter`
    """
	...

def listCheckpointDocuments(*args: _Any) -> _Any:
	""" List the existing checkpoint documents specified by the "checkpointName" """
	...

def listCheckpoints(*args: _Any) -> _Any:
	""" List the existing checkpoints """
	...

def listClusterMemberTemplates(*args: _Any) -> _Any:
	""" No description available """
	...

def listCompUnits(*args: _Any) -> _Any:
	""" List composition units belonging to a specified business-level application. """
	...

def listConnectionFactoryInterfaces(*args: _Any) -> _Any:
	""" List all of the defined connection factory interfaces on the specified J2C resource adapter. """
	...

def listControlOps(*args: _Any) -> _Any:
	""" Lists control operations defined for a business-level application and its composition units. """
	...

def listCoreGroupServers(*args: _Any) -> _Any:
	""" Returns a list of core group servers. """
	...

def listCoreGroups(*args: _Any) -> _Any:
	""" Return a collection of core groups that are related to the specified core group. """
	...

def listDatasources(*args: _Any) -> _Any:
	""" List the datasources that are contained in the specified scope. 
	
	Example:
	    ```pycon
		>>> print AdminTask.listDatasources()
        DUMMYDS(cells/myCell/clusters/myCluster|resources.xml#DataSource_1599813633144)
        DUMMYDB2(cells/myCell/clusters/myCluster|resources.xml#DataSource_1621589409106)
        DUMMYDB24LUCAXA(cells/myCell/clusters/myCluster|resources.xml#DataSource_1678720288191)
        test_cluster_datasource(cells/myCell/clusters/myCluster|resources.xml#DataSource_1696520870045)
        DefaultEJBTimerDataSource(cells/myCell/nodes/myNode2/servers/US00EBASG38|resources.xml#DataSource_1000001)
        DefaultEJBTimerDataSource(cells/myCell/nodes/myNode1/servers/US00EBASG37|resources.xml#DataSource_1000001)
        DefaultEJBTimerDataSource(cells/myCell/applications/commsvc.ear/deployments/commsvc|resources.xml#DataSource_1228749623069)
        wsadmin>
        ```
	"""
	...

def listDescriptiveProps(*args: _Any) -> _Any:
	""" List descriptive properties under an object. """
	...

def listDisabledSessionCookie(*args: _Any) -> _Any:
	""" Lists the sets of cookie configurations that will not be able to be programmatically modified """
	...

def listDynamicClusterIsolationGroupMembers(*args: _Any) -> _Any:
	""" List Dynamic Cluster isolation group members """
	...

def listDynamicClusterIsolationGroups(*args: _Any) -> _Any:
	""" List Dynamic Cluster isolation groups """
	...

def listDynamicClusters(*args: _Any) -> _Any:
	""" List all dynamic clusters in the cell """
	...

def listDynamicSSLConfigSelections(*args: _Any) -> _Any:
	""" List all Dynamic SSL configuration selections. """
	...

def listEditions(*args: _Any) -> _Any:
	""" Use this command to list all the editions for a particular application. """
	...

def listElasticityActions(*args: _Any) -> _Any:
	""" Command to list all elasticity actions """
	...

def listEligibleBridgeInterfaces(*args: _Any) -> _Any:
	""" Returns a collection of node, server and transport channel chain combinations that are eligible to become bridge interfaces for the specified core group access point. """
	...

def listExternalBundleRepositories(*args: _Any) -> _Any:
	""" Lists the external bundle repositories in the configuration. """
	...

def listForeignServerTypes(*args: _Any) -> _Any:
	""" Use this command to show all of the middleware server types """
	...

def listGroupIDsOfAuthorizationGroup(*args: _Any) -> _Any:
	""" list all the group IDs in an AuthorizationGroup """
	...

def listGroupsForNamingRoles(*args: _Any) -> _Any:
	""" List the groups and special subjects from all naming roles. """
	...

def listGroupsInBusConnectorRole(*args: _Any) -> _Any:
	""" List the groups in the bus connector role """
	...

def listGroupsInDefaultRole(*args: _Any) -> _Any:
	""" List the groups in the default role. """
	...

def listGroupsInDestinationRole(*args: _Any) -> _Any:
	""" List the groups in the specified role in the destination security space role for the given destination. """
	...

def listGroupsInForeignBusRole(*args: _Any) -> _Any:
	""" List the groups in the specified role in the foreign bus security space role for the given bus. """
	...

def listGroupsInTopicRole(*args: _Any) -> _Any:
	""" Lists the groups in the specified topic role for the specified topic space. """
	...

def listGroupsInTopicSpaceRootRole(*args: _Any) -> _Any:
	""" Lists the groups in the specified topic space role for the specified topic space. """
	...

def listHealthActions(*args: _Any) -> _Any:
	""" Command to list all health actions """
	...

def listHealthPolicies(*args: _Any) -> _Any:
	""" Command to list all health policies """
	...

def listIdMgrCustomProperties(*args: _Any) -> _Any:
	""" Returns custom properties of specified repository configuration. """
	...

def listIdMgrGroupsForRoles(*args: _Any) -> _Any:
	""" Lists the uniqueName of groups for each role. """
	...

def listIdMgrLDAPAttrs(*args: _Any) -> _Any:
	""" Lists the name of all configured attributes for the specified LDAP repository. """
	...

def listIdMgrLDAPAttrsNotSupported(*args: _Any) -> _Any:
	""" Lists the details of all virtual member manager properties not supported by the specified LDAP repository. """
	...

def listIdMgrLDAPBackupServers(*args: _Any) -> _Any:
	""" Lists the backup LDAP servers. """
	...

def listIdMgrLDAPEntityTypes(*args: _Any) -> _Any:
	""" Lists the name of all configured entity types for the specified LDAP repository. """
	...

def listIdMgrLDAPExternalIdAttrs(*args: _Any) -> _Any:
	""" Lists the details of all LDAP attributes used as an external ID. """
	...

def listIdMgrLDAPServers(*args: _Any) -> _Any:
	""" Lists all the configured primary LDAP servers. """
	...

def listIdMgrPropertyExtensions(*args: _Any) -> _Any:
	""" Lists the properties that have been extended for one or more entity types. """
	...

def listIdMgrRealmBaseEntries(*args: _Any) -> _Any:
	""" Lists all base entries of the specified realm. """
	...

def listIdMgrRealmDefaultParents(*args: _Any) -> _Any:
	""" Lists the mapping of default parent uniqueName for all entity types in a specified realm. If realm name is not specified, default realm is used. """
	...

def listIdMgrRealmURAttrMappings(*args: _Any) -> _Any:
	""" Returns mappings between user and group attributes of user registry to virtual member manager properties for a realm. """
	...

def listIdMgrRealms(*args: _Any) -> _Any:
	""" Lists the name of configured realms. """
	...

def listIdMgrRepositories(*args: _Any) -> _Any:
	""" Lists names, types, and hostnames of all the configured repositories. """
	...

def listIdMgrRepositoryBaseEntries(*args: _Any) -> _Any:
	""" Returns base entries for a specified repository. """
	...

def listIdMgrSupportedDBTypes(*args: _Any) -> _Any:
	""" Returns a list of supported database types. """
	...

def listIdMgrSupportedEntityTypes(*args: _Any) -> _Any:
	""" Lists all the configured supported entity types. """
	...

def listIdMgrSupportedLDAPServerTypes(*args: _Any) -> _Any:
	""" Returns list of supported LDAP server types. """
	...

def listIdMgrSupportedMessageDigestAlgorithms(*args: _Any) -> _Any:
	""" Returns a list of supported message digest algorithms. """
	...

def listIdMgrUsersForRoles(*args: _Any) -> _Any:
	""" Lists the uniqueName of users for each role. """
	...

def listInheritDefaultsForDestination(*args: _Any) -> _Any:
	""" List inherit defaults for destination (deprecated - use isInheritDefaultsForDestination instead) """
	...

def listInheritReceiverForTopic(*args: _Any) -> _Any:
	""" List Inherit Receiver For topic (deprecated - use isInheritReceiverForTopic instead) """
	...

def listInheritSenderForTopic(*args: _Any) -> _Any:
	""" List Inherit Sender For topic (deprecated - use isInheritSenderForTopic instead) """
	...

def listInterceptors(*args: _Any) -> _Any:
	""" List interceptors from the global security configuration or from a security domain. """
	...

def listJ2CActivationSpecs(*args: _Any) -> _Any:
	""" List the J2C activation specifications that have a specified message listener type defined in the specified J2C resource adapter. """
	...

def listJ2CAdminObjects(*args: _Any) -> _Any:
	""" List the J2C administrative objects that have a specified administrative object interface defined in the specified J2C resource adapter. """
	...

def listJ2CConnectionFactories(*args: _Any) -> _Any:
	""" List J2C connection factories that have a specified connection factory interface defined in the specified J2C resource adapter. """
	...

def listJAASLoginEntries(*args: _Any) -> _Any:
	""" List JAAS login entries from the administrative security configuration or from an application security domain. """
	...

def listJAXWSHandlerLists(*args: _Any) -> _Any:
	""" List the JAX-WS Handler Lists at a given cell scope """
	...

def listJAXWSHandlers(*args: _Any) -> _Any:
	""" List the JAX-WS Handlers at a given cell scope """
	...

def listJDBCProviders(*args: _Any) -> _Any:
	""" List the JDBC providers that are contained in the specified scope. """
	...

def listJSFImplementation(*args: _Any) -> _Any:
	""" Lists the JavaServer Faces implementation used by the WebSphere runtime for an application """
	...

def listJSFImplementations(*args: _Any) -> _Any:
	""" Lists the JavaServer Faces implementations allowed by the WebSphere runtime for an application """
	...

def listJobManagers(*args: _Any) -> _Any:
	""" List all JobManagers which a given managed node is registered with """
	...

def listJobSchedulerProperties(*args: _Any) -> _Any:
	""" list properties of the job scheduler """
	...

def listKeyFileAliases(*args: _Any) -> _Any:
	""" List personal certificate aliases in a keystore file """
	...

def listKeyManagers(*args: _Any) -> _Any:
	""" List key managers within a give scope. """
	...

def listKeyReferences(*args: _Any) -> _Any:
	""" Lists key references for the keys in a keySet. """
	...

def listKeySetGroups(*args: _Any) -> _Any:
	""" List key set groups within a scope. """
	...

def listKeySets(*args: _Any) -> _Any:
	""" List key sets within a scope. """
	...

def listKeySizes(*args: _Any) -> _Any:
	""" Displays a list of certificate key sizes. """
	...

def listKeyStoreTypes(*args: _Any) -> _Any:
	""" List the supported keystore types. """
	...

def listKeyStoreUsages(*args: _Any) -> _Any:
	""" Returns a list of valid keystore usage types.  A usage is a way to identify how the keystore is intended to be used. """
	...

def listKeyStores(*args: _Any) -> _Any:
	""" List keystore objects in a particular scope. """
	...

def listKrbAuthMechanism(*args: _Any) -> _Any:
	""" The KRB5 authentication mechanism security object field in the security configuration file is displayed. """
	...

def listLMServices(*args: _Any) -> _Any:
	""" Use the "listLMServices" command to list the created local mapping services. """
	...

def listLocalRepositoryBundles(*args: _Any) -> _Any:
	""" Lists all bundles in the internal bundle repository. """
	...

def listLoginConfigs(*args: _Any) -> _Any:
	""" Lists the login module configuration aliases. """
	...

def listLoginModules(*args: _Any) -> _Any:
	""" List all login modules for a JAAS login entry. """
	...

def listLongRunningSchedulerProperties(*args: _Any) -> _Any:
	""" (Deprecated) list properties of the long-running scheduler. Use listJobSchedulerProperties. """
	...

def listManagedNodes(*args: _Any) -> _Any:
	""" Use this command to list all registered managed nodes in the admin agent, or to list all federated nodes in the deployment manager. """
	...

def listManagementScopeOptions(*args: _Any) -> _Any:
	""" Returns a list of all cell, node, server, cluster, and nodegroups management scopes in the configuration. """
	...

def listManagementScopes(*args: _Any) -> _Any:
	""" List all management scopes. """
	...

def listMessageListenerTypes(*args: _Any) -> _Any:
	""" List all of the defined message listener types on the specified J2C resource adapter. """
	...

def listMiddlewareAppEditions(*args: _Any) -> _Any:
	""" Use this command to list all editions for a middleware application. """
	...

def listMiddlewareAppWebModules(*args: _Any) -> _Any:
	""" Use this command to list the web modules for a middleware application. """
	...

def listMiddlewareApps(*args: _Any) -> _Any:
	""" Use this command to list all middleware applications. """
	...

def listMiddlewareDescriptorVersions(*args: _Any) -> _Any:
	""" Use this command to list which versions have specific information provided in the middleware descriptor. """
	...

def listMiddlewareDescriptors(*args: _Any) -> _Any:
	""" Use this command to list the names of all installed middleware descriptors """
	...

def listMiddlewareServerTypes(*args: _Any) -> _Any:
	""" Use this command to show all of the middleware server types """
	...

def listMiddlewareServers(*args: _Any) -> _Any:
	""" Use this command to show all of the servers of the specified server type.  If no server type is specified, then all servers are shown """
	...

def listMiddlewareTargets(*args: _Any) -> _Any:
	""" Use this command to list the deployment targets for a middleware application. """
	...

def listNodeGroupProperties(*args: _Any) -> _Any:
	""" list properties of a node group """
	...

def listNodeGroups(*args: _Any) -> _Any:
	""" list node groups containing given node, or list all node groups if no target node is given """
	...

def listNodes(*args: _Any) -> _Any:
	""" list all the nodes in the cell or on a specified nodeGroup. """
	...

def listOSGiExtensions(*args: _Any) -> _Any:
	""" Shows the current extensions attached to the composition unit. """
	...

def listPHPServers(*args: _Any) -> _Any:
	""" Use this command to list PHP Servers. """
	...

def listPasswordEncryptionKeys(*args: _Any) -> _Any:
	""" Displays the list of key alias names and the current encryption key in the specified keystore file. The first item in the list is the current encryption key. """
	...

def listPersonalCertificates(*args: _Any) -> _Any:
	""" The list of personal certificates in a given keystore. """
	...

def listPolicySets(*args: _Any) -> _Any:
	""" The listPolicySets command returns a list of all existing policy sets. """
	...

def listPolicyTypes(*args: _Any) -> _Any:
	""" The listPolicyTypes command returns a list of the names of the policies configured in the system, in a policy set, or in a binding. """
	...

def listPureQueryBindFiles(*args: _Any) -> _Any:
	""" List the pureQuery bind files in an installed application. """
	...

def listRegistryGroups(*args: _Any) -> _Any:
	""" Returns a list of groups in a security realm, security domain, or resource. """
	...

def listRegistryUsers(*args: _Any) -> _Any:
	""" Returns a list of users in the specified security realm, security domain, or resource. """
	...

def listRemoteCellsFromIntelligentManagement(*args: _Any) -> _Any:
	""" Command to list remote cells from Intelligent Management """
	...

def listReplicationDomainReferences(*args: _Any) -> _Any:
	""" List search object that participates in a specific data replication domain.  An object participates in a data replication domain if the object references the provided data replication domain name.  The command returns the objects that reference the data replication domain name regardless of whether replication is enabled or disabled for that object. """
	...

def listResourcesForGroupID(*args: _Any) -> _Any:
	""" List all the objects that a given group has access to. """
	...

def listResourcesForUserID(*args: _Any) -> _Any:
	""" List all the objects that a given user has access to. """
	...

def listResourcesInSecurityDomain(*args: _Any) -> _Any:
	""" List all resources mapped to the specified security domain. """
	...

def listResourcesOfAuthorizationGroup(*args: _Any) -> _Any:
	""" List all the resources within the given Authorization Group. """
	...

def listRoutingRules(*args: _Any) -> _Any:
	""" Use this command to list routing policy rules. """
	...

def listRuleset(*args: _Any) -> _Any:
	""" Use this command to list a ruleset. """
	...

def listSAMLIssuerConfig(*args: _Any) -> _Any:
	""" List SAML Issuer Configuration data """
	...

def listSIBDestinations(*args: _Any) -> _Any:
	""" List destinations belonging to a bus. """
	...

def listSIBEngines(*args: _Any) -> _Any:
	""" List messaging engines. """
	...

def listSIBForeignBuses(*args: _Any) -> _Any:
	""" List the SIB foreign buses. """
	...

def listSIBJMSActivationSpecs(*args: _Any) -> _Any:
	""" List activation specifications on the SIB JMS resource adapter in given scope. """
	...

def listSIBJMSConnectionFactories(*args: _Any) -> _Any:
	""" List all SIB JMS connection factories of the specified type at the specified scope. """
	...

def listSIBJMSQueues(*args: _Any) -> _Any:
	""" List all SIB JMS queues at the specified scope. """
	...

def listSIBJMSTopics(*args: _Any) -> _Any:
	""" List all SIB JMS topics at the specified scope. """
	...

def listSIBLinks(*args: _Any) -> _Any:
	""" List the SIB links. """
	...

def listSIBMQLinks(*args: _Any) -> _Any:
	""" List the WebSphere MQ links. """
	...

def listSIBMediations(*args: _Any) -> _Any:
	""" List the mediations on a bus. """
	...

def listSIBNominatedBootstrapMembers(*args: _Any) -> _Any:
	""" Lists all the servers or clusters that have been nominated for bootstrap into the specified bus. """
	...

def listSIBPermittedChains(*args: _Any) -> _Any:
	""" Lists the permitted chains for the specified bus. """
	...

def listSIBWMQServerBusMembers(*args: _Any) -> _Any:
	""" List all WebSphere MQ servers. """
	...

def listSIBWMQServers(*args: _Any) -> _Any:
	""" List all WebSphere MQ servers. """
	...

def listSIBusMembers(*args: _Any) -> _Any:
	""" List the members on a bus. """
	...

def listSIBuses(*args: _Any) -> _Any:
	""" List all buses in the cell. """
	...

def listSSLCiphers(*args: _Any) -> _Any:
	""" List of ciphers. """
	...

def listSSLConfigGroups(*args: _Any) -> _Any:
	""" List all SSL configuration groups. """
	...

def listSSLConfigProperties(*args: _Any) -> _Any:
	""" List the properties for a given SSL configuration. """
	...

def listSSLConfigs(*args: _Any) -> _Any:
	""" List SSL configurations for a specific management scope. """
	...

def listSSLProtocolTypes(*args: _Any) -> _Any:
	""" Lists the SSL protocols valid for the current FIPS configuration. If FIPS is not enabled, then the full list of valid SSL protocols are returned. """
	...

def listSSLRepertoires(*args: _Any) -> _Any:
	""" List all SSLConfig instances that can be associated with an SSLInboundChannel """
	...

def listSTSAssignedEndpoints(*args: _Any) -> _Any:
	""" Query the STS for a list of assigned endpoints. """
	...

def listSTSConfigurationProperties(*args: _Any) -> _Any:
	""" List the configuration properties under a configuration group. """
	...

def listSTSConfiguredTokenTypes(*args: _Any) -> _Any:
	""" Query the STS for a list of configured token types. """
	...

def listSTSEndpointTokenTypes(*args: _Any) -> _Any:
	""" List assigned token types for an endpoint. """
	...

def listSTSProperties(*args: _Any) -> _Any:
	""" List the configuration properties under a configuration group. """
	...

def listSecurityDomains(*args: _Any) -> _Any:
	""" Lists all security domains. """
	...

def listSecurityDomainsForResources(*args: _Any) -> _Any:
	""" Returns a list of resources and their associated domain for each resource provided. """
	...

def listSecurityRealms(*args: _Any) -> _Any:
	""" List all security realms in the configuration from global security and the security domains. """
	...

def listServerPorts(*args: _Any) -> _Any:
	""" Displays a list of ports that is used by a particular server, including the node name, server name, named endpoint, and host and port values. """
	...

def listServerTemplates(*args: _Any) -> _Any:
	""" Lists the available Server Templates """
	...

def listServerTypes(target_node: _Union[ConfigurationObjectName, str] = "") -> MultilineList[str]:
	""" Lists the available serverTypes that have a template.
	
	Args:
	    target_node (ConfigurationObjectName, optional): The node name or configuration id whose available serverTypes are to be displayed. Defaults to "".
	
    Returns:
        server_types (MultilineList[str]): A list of all the available serverTypes.
        
	Example:
	    ```pycon
        >>> print(AdminTask.listServerTypes())
        TOMCAT_SERVER
        APPLICATION_SERVER
        LIBERTY_SERVER
        CUSTOMHTTP_SERVER
        WASCE_SERVER
        ONDEMAND_ROUTER
        APACHE_SERVER
        WEB_SERVER
        PROXY_SERVER
        WASAPP_SERVER
        JBOSS_SERVER
        WEBLOGIC_SERVER
        GENERIC_SERVER
        PHP_SERVER
        ```
		
    Question: Documentation unclear
        The documentation is not clear on whether the `target_node` parameter must be the node name or configuration ID (or both).
		Both work, but it is not clear if this is intended or not.
	"""
	...

def listServers(arguments: str) -> MultilineList[ConfigurationObjectName]:
	""" List servers of specified server type and node name. 
	
	If node name is not specified, the whole cell will be searched. 
	If the server type is not specified servers of all types are returned.
	
	The available parameters are:
	- serverType: The ServerType (eg. `APPLICATION_SERVER`)
    - nodeName: The Node Name (eg. `myNode`)
	
	Args:
        arguments (str): The arguments to pass to the `listServers` command in the form `[ -paramName paramValue ]` 
		    (the square brackets are not required).
		
    Returns:
        servers (MultilineList[ConfigurationObjectName]): A list of all the servers matching the specified parameters.

	Example:
        ```pycon
		>>> print(AdminTask.listServers('[-serverType DEPLOYMENT_MANAGER]'))
        dmgr(cells/myCell/nodes/myNode/servers/dmgr|server.xml)
		
		>>> print(AdminTask.listServers('-serverType APPLICATION_SERVER -nodeName myNode1'))
        server1(cells/myCell/nodes/myNode1/servers/server1|server.xml#Server_1)
        ```

    !!! abstract "See also"
        - [`AdminTask.listServerTypes()`][wsadmin_type_hints.AdminTask.listServerTypes]
	"""
	...

def listServiceMaps(*args: _Any) -> _Any:
	""" Use the "listServiceMaps" command to list the installed service maps. """
	...

def listServiceRules(*args: _Any) -> _Any:
	""" Use this command to list service policy rules. """
	...

def listServices(*args: _Any) -> _Any:
	""" Lists the services based on a generic query properties. It provides more generic query functions than listWebServices, listWebServiceEndpoints, listWebServiceOperations, and getWebService commands. """
	...

def listSignatureAlgorithms(*args: _Any) -> _Any:
	""" List signature algorithms available for the current FIPS configuration. If FIPS is not enabled, then the full list of valid Signature Algorithms are returned. """
	...

def listSignerCertificates(*args: _Any) -> _Any:
	""" The list of signer certificates in a keystore. """
	...

def listSqljProfiles(*args: _Any) -> _Any:
	""" List the serialized SQLJ profiles that are in an installed application. """
	...

def listSupportedJPASpecifications(*args: _Any) -> _Any:
	""" Lists JPA Specification levels supported by this version of WebSphere. """
	...

def listSupportedJaxrsProviders(*args: _Any) -> _Any:
	""" Lists JAXRS Providers supported by this version of WebSphere. """
	...

def listSupportedPolicySets(*args: _Any) -> _Any:
	""" listSupportedPolicySetsCmdDesc """
	...

def listTAMSettings(*args: _Any) -> _Any:
	""" This command lists the current embedded Tivoli Access Manager configuration settings. """
	...

def listTCPEndPoints(*args: _Any) -> _Any:
	""" Lists all NamedEndPoints that can be associated with a TCPInboundChannel """
	...

def listTCPThreadPools(*args: _Any) -> _Any:
	""" Lists all ThreadPools that can be associated with a TCPInboundChannel or TCPOutboundChannel """
	...

def listTraceRulesForIntelligentManagement(*args: _Any) -> _Any:
	""" List trace rules for Intelligent Management """
	...

def listTrustManagers(*args: _Any) -> _Any:
	""" List trust managers. """
	...

def listTrustedRealms(*args: _Any) -> _Any:
	""" List trusted realms trusted by a security realm, resource, or security domain. """
	...

def listUDPEndPoints(*args: _Any) -> _Any:
	""" Lists all the NamedEndPoints endpoints that can be associated with a UDPInboundChannel """
	...

def listUnmanagedNodes(*args: _Any) -> _Any:
	""" Use this command to list all unmanaged nodes in the cell. """
	...

def listUserIDsOfAuthorizationGroup(*args: _Any) -> _Any:
	""" list all the users IDs in an AuthorizationGroup """
	...

def listUsersForNamingRoles(*args: _Any) -> _Any:
	""" List the users from all naming roles. """
	...

def listUsersInBusConnectorRole(*args: _Any) -> _Any:
	""" List the users in the Bus Connector Role """
	...

def listUsersInDefaultRole(*args: _Any) -> _Any:
	""" List the users in a default role. """
	...

def listUsersInDestinationRole(*args: _Any) -> _Any:
	""" List the users in the specified role in the destination security space role for the given destination. """
	...

def listUsersInForeignBusRole(*args: _Any) -> _Any:
	""" List the users in the specified role in the foreign bus security space role for the given bus. """
	...

def listUsersInTopicRole(*args: _Any) -> _Any:
	""" Lists the users in the specified topic role for the specified topic space. """
	...

def listUsersInTopicSpaceRootRole(*args: _Any) -> _Any:
	""" Lists the users in the specified topic space role for the specified topic space. """
	...

def listWASServerTypes(*args: _Any) -> _Any:
	""" Use this command to show all of the middleware server types """
	...

def listWMQActivationSpecs(*args: _Any) -> _Any:
	""" Lists the IBM MQ Activation Specification defined at the scope provided to the command. """
	...

def listWMQConnectionFactories(*args: _Any) -> _Any:
	""" Lists the IBM MQ Connection Factories defined at the scope provided to the command. """
	...

def listWMQQueues(*args: _Any) -> _Any:
	""" Lists the IBM MQ Queues defined at the scope provided to the command. """
	...

def listWMQTopics(*args: _Any) -> _Any:
	""" Lists the IBM MQ Topics defined at the scope provided to the command. """
	...

def listWSCertExpMonitor(*args: _Any) -> _Any:
	""" List all certificate expiration monitors. """
	...

def listWSNAdministeredSubscribers(*args: _Any) -> _Any:
	""" Lists all the WSNAdministeredSubscriber objects in the configuration of the target WSNServicePoint that match the specified input parameters. """
	...

def listWSNServicePoints(*args: _Any) -> _Any:
	""" Lists all the WSNServicePoint objects in the configuration of the target WSNService that match the specified input parameters. """
	...

def listWSNServices(*args: _Any) -> _Any:
	""" Lists all the WSNService objects in the configuration that match the specified input parameters. """
	...

def listWSNTopicDocuments(*args: _Any) -> _Any:
	""" Lists all the WSNTopicDocument objects in the configuration of the target WSNTopicNamespace that match the specified input parameters. """
	...

def listWSNTopicNamespaces(*args: _Any) -> _Any:
	""" Lists all the WSNTopicNamespace objects in the configuration of the target WSNService that match the specified input parameters. """
	...

def listWSNotifiers(*args: _Any) -> _Any:
	""" List all notifiers. """
	...

def listWSSchedules(*args: _Any) -> _Any:
	""" List all schedules. """
	...

def listWebServerRoutingRules(*args: _Any) -> _Any:
	""" Use this command to list routing rules and their associated properties. """
	...

def listWebServiceEndpoints(*args: _Any) -> _Any:
	""" Lists the Web service endpoints that are port names defined in a Web service in an enterprise application. """
	...

def listWebServiceOperations(*args: _Any) -> _Any:
	""" Lists the Web service operations defined in a logical endpoint. """
	...

def listWebServices(*args: _Any) -> _Any:
	""" Lists the deployed Web services in enterprise applications. If there is no application name supplied, then all the Web services in the enterprise applications will are be listed. """
	...

def makeNonSystemTemplate(*args: _Any) -> _Any:
	""" makeNonSystemTemplate """
	...

def manageWMQ(*args: _Any) -> _Any:
	""" Provides the ability to manage the settings associated with the IBM MQ resource adapter installed at a particular scope. """
	...

def mapAuditGroupIDsOfAuthorizationGroup(*args: _Any) -> _Any:
	""" Maps the special subjects to actual users in the registry. """
	...

def mapGroupsToAdminRole(*args: _Any) -> _Any:
	""" Map groupids to one or more admin role in the authorization group. """
	...

def mapGroupsToAuditRole(*args: _Any) -> _Any:
	""" Map groupids to one or more audit role in the authorization group. """
	...

def mapGroupsToNamingRole(*args: _Any) -> _Any:
	""" Map groups or special subjects or both to the naming roles """
	...

def mapIdMgrGroupToRole(*args: _Any) -> _Any:
	""" Maps the group to the specified role of virtual member manager. """
	...

def mapIdMgrUserToRole(*args: _Any) -> _Any:
	""" Maps the user to the specified role of virtual member manager. """
	...

def mapResourceToSecurityDomain(*args: _Any) -> _Any:
	""" Map a resource to a security domain. """
	...

def mapUsersToAdminRole(*args: _Any) -> _Any:
	""" Map userids to one or more admin role in the authorization group. """
	...

def mapUsersToAuditRole(*args: _Any) -> _Any:
	""" Map userids to one or more audit role in the authorization group. """
	...

def mapUsersToNamingRole(*args: _Any) -> _Any:
	""" Map users to the naming roles """
	...

def mediateSIBDestination(*args: _Any) -> _Any:
	""" Mediate a destination. """
	...

def migrateServerMEtoCluster(*args: _Any) -> _Any:
	""" This command will migrate a server messaging engine to a cluster messaging engine. It will not modify the messaging engine message store. Please ensure that the message store is suitable for the new clustered environment. If it is not, the migrated engine must be re-configured with a suitable message store before it is started, or the engine may fail to start. """
	...

def migrateWMQMLP(*args: _Any) -> _Any:
	""" Migrates a IBM MQ message listener port definition to an activation specification definition. """
	...

def modifyAuditEmitter(*args: _Any) -> _Any:
	""" Modifies an audit service provider implementation in the audit.xml file """
	...

def modifyAuditEncryptionConfig(*args: _Any) -> _Any:
	""" Modifies the audit record encryption configuration. """
	...

def modifyAuditEventFactory(*args: _Any) -> _Any:
	""" Modifies an entry in the audit.xml to reference the configuration of an audit event factory implementation of the Audit Event Factory interface. """
	...

def modifyAuditFilter(*args: _Any) -> _Any:
	""" Modifies an audit specification entry in the audit.xml that matches the reference Id. """
	...

def modifyAuditKeyStore(*args: _Any) -> _Any:
	""" Modifies a Keystore object. """
	...

def modifyAuditNotification(*args: _Any) -> _Any:
	""" Modifies an audit notification. """
	...

def modifyAuditNotificationMonitor(*args: _Any) -> _Any:
	""" Modifies the audit notification monitor specified by the reference id. """
	...

def modifyAuditPolicy(*args: _Any) -> _Any:
	""" Modifies the audit policy attributes. """
	...

def modifyAuditSigningConfig(*args: _Any) -> _Any:
	""" Modifies the audit record signing configuration. """
	...

def modifyAuthDataEntry(*args: _Any) -> _Any:
	""" Modify an authentication data entry """
	...

def modifyCAClient(*args: _Any) -> _Any:
	""" Modifies a certificate authority (CA) client configurator object. """
	...

def modifyDescriptiveProp(*args: _Any) -> _Any:
	""" Modify a descriptive property under an object. """
	...

def modifyDisabledSessionCookie(*args: _Any) -> _Any:
	""" Modifies an existing cookie configuration """
	...

def modifyDynamicClusterIsolationProperties(*args: _Any) -> _Any:
	""" Modify Dynamic Cluster isolation properties """
	...

def modifyElasticityAction(*args: _Any) -> _Any:
	""" Command to modify a elasticity action """
	...

def modifyExternalBundleRepository(*args: _Any) -> _Any:
	""" Modifies the named external bundle repository with the given parameters. Unspecified parameters keep their existing values. To remove an existing value, specify an empty string for the parameter. """
	...

def modifyForeignServerProperty(*args: _Any) -> _Any:
	""" Use this command to modify a property on a middleware server """
	...

def modifyHealthAction(*args: _Any) -> _Any:
	""" Command to modify a health action """
	...

def modifyHealthPolicy(*args: _Any) -> _Any:
	""" Command to modify a health policy """
	...

def modifyIntelligentManagement(*args: _Any) -> _Any:
	""" Command to modify Intelligent Management properties """
	...

def modifyIntelligentManagementConnectorCluster(*args: _Any) -> _Any:
	""" Command to modify properties of ConnectorCluster """
	...

def modifyJAXWSHandler(*args: _Any) -> _Any:
	""" Modify a JAX-WS Handler """
	...

def modifyJAXWSHandlerList(*args: _Any) -> _Any:
	""" Modify a JAX-WS Handler _List """
	...

def modifyJPASpecLevel(*args: _Any) -> _Any:
	""" Changes the active JPA specification level for a Server or ServerCluster.The operation requires either an ObjectName referencing the target object, or parameters identifying the target node and server.  The specLevel parameter must always be specified. """
	...

def modifyJSFImplementation(*args: _Any) -> _Any:
	""" Modifies the JavaServer Faces implementation used by the WebSphere runtime for an application """
	...

def modifyJaspiProvider(*args: _Any) -> _Any:
	""" Modify configuration data for a given authentication provider. """
	...

def modifyJaxrsProvider(*args: _Any) -> _Any:
	""" Changes the active JAXRS Provider for a Server or ServerCluster.The operation requires either an ObjectName referencing the target object, or parameters identifying the target node and server.  The Provider parameter must always be specified. """
	...

def modifyJobSchedulerAttribute(*args: _Any) -> _Any:
	""" modify a job scheduler attribute """
	...

def modifyJobSchedulerProperty(*args: _Any) -> _Any:
	""" modify the property of the job scheduler """
	...

def modifyKeyManager(*args: _Any) -> _Any:
	""" Modify a key manager. """
	...

def modifyKeySet(*args: _Any) -> _Any:
	""" Modify a Key Sets attributes. """
	...

def modifyKeySetGroup(*args: _Any) -> _Any:
	""" Modify the a key set group. """
	...

def modifyKeyStore(*args: _Any) -> _Any:
	""" Modifies a Keystore object. """
	...

def modifyKrbAuthMechanism(*args: _Any) -> _Any:
	""" The KRB5 authentication mechanism security object field in the security configuration file is modified based on the user input. """
	...

def modifyLongRunningSchedulerAttribute(*args: _Any) -> _Any:
	""" (Deprecated) modify a long-running scheduler attribute. Use modifyJobSchedulerAttribute. """
	...

def modifyLongRunningSchedulerProperty(*args: _Any) -> _Any:
	""" (Deprecated) modify the property of the long-running scheduler. Use modifyJobSchedulerProperty. """
	...

def modifyManagedNodeGroupInfo(*args: _Any) -> _Any:
	""" Update information for a group of managed nodes. (deprecated) """
	...

def modifyManagedNodeProperties(*args: _Any) -> _Any:
	""" Modify properties associated with a specific managed node. (deprecated) """
	...

def modifyMiddlewareAppWebModule(*args: _Any) -> _Any:
	""" Use this command to modify the web module of a middleware application. """
	...

def modifyMiddlewareDescriptorDiscoveryInterval(*args: _Any) -> _Any:
	""" Use this command to modify the discovery interval of the specified middleware descriptor """
	...

def modifyMiddlewareDescriptorProperty(*args: _Any) -> _Any:
	""" Use this command to modify a property of a specific version of the middleware platform that the descriptor represents.  If no version is specified, the "default" version will be updated. """
	...

def modifyNodeGroup(*args: _Any) -> _Any:
	""" modify a node group configuration """
	...

def modifyNodeGroupProperty(*args: _Any) -> _Any:
	""" modify the property of a node group """
	...

def modifyPHPApp(*args: _Any) -> _Any:
	""" Use this command to modify a PHP application. """
	...

def modifyPasswordEncryption(*args: _Any) -> _Any:
	""" Modifies the configuration of the password encryption. Note that the original value is unchanged unless the value is set by the parameter. To change the value to the default, use a blank string (""). """
	...

def modifyPolicy(*args: _Any) -> _Any:
	""" Modify a policy that matches the provided policy name. """
	...

def modifyRemoteCellForIntelligentManagement(*args: _Any) -> _Any:
	""" Command to modify remote cell connectors for Intelligent Management """
	...

def modifySIBDestination(*args: _Any) -> _Any:
	""" Modify bus destination. """
	...

def modifySIBEngine(*args: _Any) -> _Any:
	""" Modify a messaging engine. """
	...

def modifySIBForeignBus(*args: _Any) -> _Any:
	""" Modify a SIB foreign bus. """
	...

def modifySIBJMSActivationSpec(*args: _Any) -> _Any:
	""" Modify the attributes of the given SIB JMS activation specification. """
	...

def modifySIBJMSConnectionFactory(*args: _Any) -> _Any:
	""" Modify the attributes of the supplied SIB JMS connection factory using the supplied attribute values. """
	...

def modifySIBJMSQueue(*args: _Any) -> _Any:
	""" Modify the attributes of the supplied SIB JMS queue using the supplied attribute values. """
	...

def modifySIBJMSTopic(*args: _Any) -> _Any:
	""" Modify the attributes of the supplied SIB JMS topic using the supplied attribute values. """
	...

def modifySIBLink(*args: _Any) -> _Any:
	""" Modify an existing SIB link. """
	...

def modifySIBMQLink(*args: _Any) -> _Any:
	""" Modify an existing WebSphere MQ link. """
	...

def modifySIBMediation(*args: _Any) -> _Any:
	""" Modify a mediation. """
	...

def modifySIBWMQServer(*args: _Any) -> _Any:
	""" Modify a named WebSphere MQ server's attributes. """
	...

def modifySIBWMQServerBusMember(*args: _Any) -> _Any:
	""" Modify a named WebSphere MQ server bus member. """
	...

def modifySIBus(*args: _Any) -> _Any:
	""" Modify a bus. """
	...

def modifySIBusMemberPolicy(*args: _Any) -> _Any:
	""" Modify a cluster bus members messaging engine policy assistance settings. """
	...

def modifySSLConfig(*args: _Any) -> _Any:
	""" Modify a SSL configuration. """
	...

def modifySSLConfigGroup(*args: _Any) -> _Any:
	""" Modify a SSL configuration group. """
	...

def modifySecurityDomain(*args: _Any) -> _Any:
	""" Modifies a security domain's description. """
	...

def modifyServerPort(*args: _Any) -> _Any:
	""" Modifies the host or port of the named endpoint that is used by the specified server. """
	...

def modifySpnegoFilter(*args: _Any) -> _Any:
	""" This command modifies SPNEGO Web authentication Filter attributes in the security configuration. """
	...

def modifySpnegoTAIProperties(*args: _Any) -> _Any:
	""" This command modifies SPNEGO TAI properties in the security configuration. """
	...

def modifyTAM(*args: _Any) -> _Any:
	""" This command modifies the configuration for embedded Tivoli Access Manager on the WebSphere Application Server node or nodes specified. """
	...

def modifyTargetGroupInfo(*args: _Any) -> _Any:
	""" Update information for a group of Targets. """
	...

def modifyTargetProperties(*args: _Any) -> _Any:
	""" Modify properties associated with a specific Target. """
	...

def modifyTrustManager(*args: _Any) -> _Any:
	""" Modify a trust manager. """
	...

def modifyUnmanagedWebApp(*args: _Any) -> _Any:
	""" Use this command to modify an unmanaged web application. """
	...

def modifyWMQActivationSpec(*args: _Any) -> _Any:
	""" Modifies the properties of the IBM MQ Activation Specification provided to the command. """
	...

def modifyWMQConnectionFactory(*args: _Any) -> _Any:
	""" Modifies the properties of the IBM MQ Connection Factory provided to the command. """
	...

def modifyWMQQueue(*args: _Any) -> _Any:
	""" Modifies the properties of the IBM MQ Queue provided to the command. """
	...

def modifyWMQTopic(*args: _Any) -> _Any:
	""" Modifies the properties of the IBM MQ Topic provided to the command. """
	...

def modifyWSCertExpMonitor(*args: _Any) -> _Any:
	""" Modify a certificate expiration monitor. """
	...

def modifyWSNotifier(*args: _Any) -> _Any:
	""" Modify a notifier. """
	...

def modifyWSSchedule(*args: _Any) -> _Any:
	""" Modify a schedule. """
	...

def modifyWasCEApp(*args: _Any) -> _Any:
	""" Use this command to modify a WAS CE application. """
	...

def moveClusterToCoreGroup(*args: _Any) -> _Any:
	""" Move all servers in a cluster from one core group to another. """
	...

def moveServerToCoreGroup(*args: _Any) -> _Any:
	""" Move a server from one core group to another. """
	...

def populateUniqueNames(*args: _Any) -> _Any:
	""" Attempt to populate any missing unique name entries in the authorization model for the specified bus using its user repository. """
	...

def prepareKeysForCellProfile(*args: _Any) -> _Any:
	""" Prepare keys and keystores for Cell profile creation. """
	...

def prepareKeysForSingleProfile(*args: _Any) -> _Any:
	""" Prepare keys and keystores for a profile creation. """
	...

def processPureQueryBindFiles(*args: _Any) -> _Any:
	""" Process the pureQuery bind files that are in an installed application.  Bind static SQL packages in a database.  Refer to the information center documentation for the pureQuery bind utility. """
	...

def processSqljProfiles(*args: _Any) -> _Any:
	""" Process the serialized SQLJ profiles that are in an installed application.  Customize the profiles with information for run time and bind static SQL packages in a database.  Refer to the DB2 information center documentation for the commands db2sqljcustomize and db2sqljbind. """
	...

def propagatePolicyToJACCProvider(*args: _Any) -> _Any:
	""" Propagate the security policies of the applications to the JACC provider. """
	...

def publishSIBWSInboundService(*args: _Any) -> _Any:
	""" Publish an inbound service to a UDDI registry. """
	...

def purgeUserFromAuthCache(*args: _Any) -> _Any:
	""" Purges a user from the auth cache for a security domain; if no security domain is specified, the user will be purged from the admin security domain """
	...

def queryCACertificate(*args: _Any) -> _Any:
	""" Queries a certificate authority (CA) to see if a certificate is complete. """
	...

def queryJobs(*args: _Any) -> _Any:
	""" Query for previously submitted jobs. """
	...

def queryManagedNodeGroups(*args: _Any) -> _Any:
	""" This command is used to query groups of Managed Nodes. (deprecated) """
	...

def queryManagedNodes(*args: _Any) -> _Any:
	""" Queries for all the managed nodes registered with the job manager. (deprecated) """
	...

def queryManagedResources(*args: _Any) -> _Any:
	""" Queries for all managed resources. """
	...

def querySCClientCacheConfiguration(*args: _Any) -> _Any:
	""" List the SC cache configuration """
	...

def querySCClientCacheCustomConfiguration(*args: _Any) -> _Any:
	""" List the SC custom properties """
	...

def querySTSDefaultTokenType(*args: _Any) -> _Any:
	""" Query the STS for the default token type. """
	...

def querySTSTokenTypeConfigurationCustomProperties(*args: _Any) -> _Any:
	""" Query the STS for the values of the custom properties for a given token type. """
	...

def querySTSTokenTypeConfigurationDefaultProperties(*args: _Any) -> _Any:
	""" Query the STS for the values of the default properties for a given token type. """
	...

def queryServerAvailability(*args: _Any) -> _Any:
	""" checks the UCF server availability indicator on specified server """
	...

def queryTargetGroups(*args: _Any) -> _Any:
	""" This command is used to query groups of targets. """
	...

def queryTargets(*args: _Any) -> _Any:
	""" Queries for all the Targets registered with the job manager. """
	...

def queryWSSDistributedCacheConfig(*args: _Any) -> _Any:
	""" List the Web Services Security distributed cache configuration properties """
	...

def queryWSSDistributedCacheCustomConfig(*args: _Any) -> _Any:
	""" List Web Services Security distributed cache configuration custom properties """
	...

def receiveCertificate(*args: _Any) -> _Any:
	""" Receive a certificate from a file. """
	...

def reconfigureTAM(*args: _Any) -> _Any:
	""" This command configures embedded Tivoli Access Manager on the WebSphere Application Server node or nodes specified. """
	...

def recoverMEConfig(*args: _Any) -> _Any:
	""" Use this command if there is no configuration data of crashed ME and user needs to recover persistent SBus ME data from message store. """
	...

def refreshCellForIntelligentManagement(*args: _Any) -> _Any:
	""" Command to refresh cell connectors for Intelligent Management """
	...

def refreshSIBWSInboundServiceWSDL(*args: _Any) -> _Any:
	""" Refresh the WSDL definition for an inbound service. """
	...

def refreshSIBWSOutboundServiceWSDL(*args: _Any) -> _Any:
	""" Refresh the WSDL definition for an outbound service. """
	...

def refreshSTS(*args: _Any) -> _Any:
	""" Reload the STS configuration dynamically. """
	...

def regenPasswordEncryptionKey(*args: _Any) -> _Any:
	""" Generates a new AES password encryption key, sets it as the current key for the encryption, and then updates the passwords with the new key. This command is disabled when the custom KeyManager class is used. """
	...

def registerApp(*args: _Any) -> _Any:
	""" Use this command to register a middleware application already installed on a server. """
	...

def registerHost(*args: _Any) -> _Any:
	""" Registers a host with the job manager. """
	...

def registerWithJobManager(*args: _Any) -> _Any:
	""" Register a managed node with a JobManager """
	...

def removeActionFromRule(*args: _Any) -> _Any:
	""" Use this command to remove an action from a rule. """
	...

def removeAutomaticEJBTimers(*args: _Any) -> _Any:
	""" This command removes automatically created persistent EJBTimers for a specific application or module on a specific server.  Refer to the product InfoCenter for scenarios where this command might be used. """
	...

def removeConditionalTraceRuleForIntelligentManagement(*args: _Any) -> _Any:
	""" Remove conditional trace for Intelligent Management """
	...

def removeCoreGroupBridgeInterface(*args: _Any) -> _Any:
	""" Delete bridge interfaces associated with a specified core group, node and server. """
	...

def removeDefaultAction(*args: _Any) -> _Any:
	""" Use this command to remove a default action from a ruleset. """
	...

def removeDefaultRoles(*args: _Any) -> _Any:
	""" Remove all default roles """
	...

def removeDestinationRoles(*args: _Any) -> _Any:
	""" Removes all destination roles defined for the specified destination in the specified bus. """
	...

def removeDisabledSessionCookie(*args: _Any) -> _Any:
	""" Removes a cookie configuration so that applications will be able to programmatically modify """
	...

def removeExternalBundleRepository(*args: _Any) -> _Any:
	""" Removes the named external bundle repository from the configuration. """
	...

def removeFeaturesFromServer(*args: _Any) -> _Any:
	""" Remove feature pack or stack product features from existing server """
	...

def removeForeignBusRoles(*args: _Any) -> _Any:
	""" Remove all foreign bus roles defined for the specified bus """
	...

def removeForeignServersFromDynamicCluster(*args: _Any) -> _Any:
	""" Remove foreign servers from dynamic cluster """
	...

def removeFromPolicySetAttachment(*args: _Any) -> _Any:
	""" The removeFromPolicySetAttachment command removes resources that apply to a policy set attachment. """
	...

def removeGroupFromAllRoles(*args: _Any) -> _Any:
	""" Removes a group from all roles defined. """
	...

def removeGroupFromBusConnectorRole(*args: _Any) -> _Any:
	""" Remove a group's permission to connect to the specified bus. """
	...

def removeGroupFromDefaultRole(*args: _Any) -> _Any:
	""" Removes a group from the specified role in the default security space role. """
	...

def removeGroupFromDestinationRole(*args: _Any) -> _Any:
	""" Removes a group from the specified destination role for the specified destination. """
	...

def removeGroupFromForeignBusRole(*args: _Any) -> _Any:
	""" Removes a group from the specified foreign bus role for the bus specified """
	...

def removeGroupFromTopicRole(*args: _Any) -> _Any:
	""" Removes a groups permission to access the topic for the specified role. """
	...

def removeGroupFromTopicSpaceRootRole(*args: _Any) -> _Any:
	""" Removes a groups permission to access the topic space for the specified role. """
	...

def removeGroupsFromAdminRole(*args: _Any) -> _Any:
	""" Remove groupids from one or more admin role in the AuthorizationGroup. """
	...

def removeGroupsFromAuditRole(*args: _Any) -> _Any:
	""" Remove groupids from one or more audit role in the AuthorizationGroup. """
	...

def removeGroupsFromNamingRole(*args: _Any) -> _Any:
	""" Remove groups or special subjects or both from a naming role """
	...

def removeIdMgrGroupsFromRole(*args: _Any) -> _Any:
	""" Removes the groups from the specified virtual member manager role. If value for groupId parameter is specified as "*" all groups mapped for the role are removed. """
	...

def removeIdMgrLDAPBackupServer(*args: _Any) -> _Any:
	""" Removes a backup LDAP server. """
	...

def removeIdMgrUsersFromRole(*args: _Any) -> _Any:
	""" Removes the users from the specified virtual member manager role. If value for userId parameter is specified as "*" all users mapped for the role are removed. """
	...

def removeJaspiProvider(*args: _Any) -> _Any:
	""" Remove the given authentication provider(s) from the security configuration. """
	...

def removeJobSchedulerProperty(*args: _Any) -> _Any:
	""" remove a property from the job scheduler """
	...

def removeLocalRepositoryBundle(*args: _Any) -> _Any:
	""" Removes a bundle from the internal bundle repository. """
	...

def removeLocalRepositoryBundles(*args: _Any) -> _Any:
	""" Removes one or more bundles from the internal bundle repository in a single operation. """
	...

def removeLongRunningSchedulerProperty(*args: _Any) -> _Any:
	""" (Deprecated) remove a property from the long-running scheduler. Use removeJobSchedulerProperty. """
	...

def removeMemberFromGroup(*args: _Any) -> _Any:
	""" Removes a member (user or group) from a group. """
	...

def removeMiddlewareAppWebModule(*args: _Any) -> _Any:
	""" Use this command to remove a web module from a middleware application. """
	...

def removeMiddlewareTarget(*args: _Any) -> _Any:
	""" Use this command to remove a deployment target from a middleware application. """
	...

def removeNodeFromNodeGroups(*args: _Any) -> _Any:
	""" remove a given node from node groups """
	...

def removeNodeGroup(*args: _Any) -> _Any:
	""" remove a node group from the configuration. """
	...

def removeNodeGroupMember(*args: _Any) -> _Any:
	""" remove a member from the node group. """
	...

def removeNodeGroupProperty(*args: _Any) -> _Any:
	""" remove a property from a node group """
	...

def removeOSGiExtension(*args: _Any) -> _Any:
	""" Removes an extension from the composition unit. """
	...

def removeOSGiExtensions(*args: _Any) -> _Any:
	""" Removes multiple extensions from the composition unit. """
	...

def removePluginPropertyForIntelligentManagement(*args: _Any) -> _Any:
	""" Remove plug-in property for Intelligent Management """
	...

def removeProductInfo(*args: _Any) -> _Any:
	""" Remove feature pack or stack product information from product info. """
	...

def removeResourceFromAuthorizationGroup(*args: _Any) -> _Any:
	""" Remove resources from an existing authorization group. """
	...

def removeResourceFromSecurityDomain(*args: _Any) -> _Any:
	""" Remove a resource from a security domain. """
	...

def removeRoutingPolicyRoutingRule(*args: _Any) -> _Any:
	""" Use this command to remove a routing rule from an existing workclass """
	...

def removeRoutingRule(*args: _Any) -> _Any:
	""" Use this command to remove a routing policy rule. """
	...

def removeRuleFromRuleset(*args: _Any) -> _Any:
	""" Use this command to remove a rule from a ruleset. """
	...

def removeSIBBootstrapMember(*args: _Any) -> _Any:
	""" Removes a nominated bootstrap server or cluster from the list of nominated bootstrap members for the bus. """
	...

def removeSIBPermittedChain(*args: _Any) -> _Any:
	""" Removes the specified chain from the list of permitted chains for the specified bus. """
	...

def removeSIBWSInboundPort(*args: _Any) -> _Any:
	""" Remove an inbound port. """
	...

def removeSIBWSOutboundPort(*args: _Any) -> _Any:
	""" Remove an outbound port. """
	...

def removeSIBusMember(*args: _Any) -> _Any:
	""" Remove a member from a bus. """
	...

def removeServicePolicyRoutingRule(*args: _Any) -> _Any:
	""" Use this command to remove a routing rule from an existing workclass """
	...

def removeServiceRule(*args: _Any) -> _Any:
	""" Use this command to remove a service policy rule. """
	...

def removeTemplates(*args: _Any) -> _Any:
	""" Removes set of templates that are not required anymore when a feature pack or stack product is removed. """
	...

def removeTrustedRealms(*args: _Any) -> _Any:
	""" Remove realms from the trusted realm list """
	...

def removeUnmanagedNode(*args: _Any) -> _Any:
	""" Use this command to remove an unmanaged node from a cell. """
	...

def removeUserFromAllRoles(*args: _Any) -> _Any:
	""" Removes a user from all roles defined. """
	...

def removeUserFromBusConnectorRole(*args: _Any) -> _Any:
	""" Remove a user's permission to connect to the specified bus. """
	...

def removeUserFromDefaultRole(*args: _Any) -> _Any:
	""" Removes a user from the specified role in the default security space role. """
	...

def removeUserFromDestinationRole(*args: _Any) -> _Any:
	""" Removes a user from the specified destination role for the specified destination. """
	...

def removeUserFromForeignBusRole(*args: _Any) -> _Any:
	""" Removes a user from the specified foreign bus role for the bus specified """
	...

def removeUserFromTopicRole(*args: _Any) -> _Any:
	""" Removes a users permission to access the topic for the specified role. """
	...

def removeUserFromTopicSpaceRootRole(*args: _Any) -> _Any:
	""" Removes a users permission to access the topic space for the specified role. """
	...

def removeUsersFromAdminRole(*args: _Any) -> _Any:
	""" Remove userids from one or more admin role in the AuthorizationGroup. """
	...

def removeUsersFromAuditRole(*args: _Any) -> _Any:
	""" Remove userids from one or more audit role in the AuthorizationGroup. """
	...

def removeUsersFromNamingRole(*args: _Any) -> _Any:
	""" Remove users from a naming role. """
	...

def removeVariable(*args: _Any) -> _Any:
	""" Remove a variable definition from the system. A variable is a configuration property that can be used to provide a parameter for some values in the system. """
	...

def removeWSGWTargetService(*args: _Any) -> _Any:
	""" removeWSGWTargetService.description """
	...

def removeWebServerRoutingRule(*args: _Any) -> _Any:
	""" Use this command to remove an existing routing rule. """
	...

def renameCell(*args: _Any) -> _Any:
	""" Change the name of the cell.  This command can only run in local mode i.e.with wsadmin conntype NONE.1. Backing up your node configuration with the backupConfig tool fromprofile_root/bin directory is recommended before you change the cell name forthat node using the renameCell command.  If you are not satisfied with theresults of the renameCell command and if the renameCell command executionfailed unexpectedly, you use the restoreConfig tool to restore your backupconfiguration.2. Back up profile_root/bin/setupCmdLine script file. The command updates thecell name in this file with the new cell name as well, but is unable to changeit back if a user decides to discard the configuration change resulting fromthis command execution. If you decide to do so, you will need to restore thefile after you discard the configuration change; otherwise, you won't be ableto start a server in this profile. """
	...

def renameIdMgrRealm(*args: _Any) -> _Any:
	""" Renames the specified realm configuration. """
	...

def renameNode(*args: _Any) -> _Any:
	""" renameNode """
	...

def renewAuditCertificate(*args: _Any) -> _Any:
	""" The task will renew a certificate as a self-signed based off the previous certificates attributes such as the common name, key size and validity. """
	...

def renewCertificate(*args: _Any) -> _Any:
	""" Renew a Certificate with a newly generated certificate. """
	...

def replaceCertificate(*args: _Any) -> _Any:
	""" Replace a Certificate with a different certificate. """
	...

def reportConfigInconsistencies(*args: _Any) -> _Any:
	""" Checks the configuation repository and reports any structural inconsistencies """
	...

def reportConfiguredPorts(*args: _Any) -> _Any:
	""" Generates a report of the ports configured in the cell """
	...

def republishEDMessages(*args: _Any) -> _Any:
	""" Use the command to republish messages from the exception destination to the original destination. The messages are picked based on the criteria provided in the command execution. """
	...

def requestCACertificate(*args: _Any) -> _Any:
	""" Sends a request to a certificate authority to create a certificate authority (CA) personal certificate. """
	...

def resetAuditSystemFailureAction(*args: _Any) -> _Any:
	""" Resets the audit system failure policy to the default, NOWARN. """
	...

def resetIdMgrConfig(*args: _Any) -> _Any:
	""" Reloads the virtual member manager configuration from the virtual member manager configuration file. """
	...

def restoreCheckpoint(*args: _Any) -> _Any:
	""" Restore the named checkpoint specified by the "checkpointName" """
	...

def resumeJob(*args: _Any) -> _Any:
	""" Resumes a previously submitted job. """
	...

def retrieveSignerFromPort(*args: _Any) -> _Any:
	""" Retrieve a signer certificate from a port and add it to the KeyStore. """
	...

def retrieveSignerInfoFromPort(*args: _Any) -> _Any:
	""" Retrieve signer information from a port. """
	...

def revokeCACertificate(*args: _Any) -> _Any:
	""" Sends a request to a certificate authority (CA) to revoke the certificate. """
	...

def rolloutEdition(*args: _Any) -> _Any:
	""" Roll-out an edition. """
	...

def searchGroups(*args: _Any) -> _Any:
	""" Searches groups. """
	...

def searchUsers(*args: _Any) -> _Any:
	""" Searches PersonAccounts. """
	...

def setActiveAuthMechanism(*args: _Any) -> _Any:
	""" This command sets the active authentication mechanism attribute in the security configuration. """
	...

def setAdminActiveSecuritySettings(*args: _Any) -> _Any:
	""" Sets the security attributes on the global administrative security configuration. """
	...

def setAdminProtocol(*args: _Any) -> _Any:
	""" Allows the user to set Administrative Protocol for a server or cell """
	...

def setAdminProtocolEnabled(*args: _Any) -> _Any:
	""" Sets an Admin Protocol enabled for a server or cell """
	...

def setAppActiveSecuritySettings(*args: _Any) -> _Any:
	""" Sets the application level security active settings. """
	...

def setAuditEmitterFilters(*args: _Any) -> _Any:
	""" Sets a list of references to defined filters for the supplied audit service provider. """
	...

def setAuditEventFactoryFilters(*args: _Any) -> _Any:
	""" Sets a list of references to defined filters for the supplied event factory. """
	...

def setAuditSystemFailureAction(*args: _Any) -> _Any:
	""" Returns the state of Security Auditing. """
	...

def setAuditorId(*args: _Any) -> _Any:
	""" Sets the auditor identity in the audit.xml file. """
	...

def setAuditorPwd(*args: _Any) -> _Any:
	""" Sets the auditor password in the audit.xml file. """
	...

def setAutoCheckpointDepth(*args: _Any) -> _Any:
	""" Set the automatic checkpoints depth value """
	...

def setAutoCheckpointEnabled(*args: _Any) -> _Any:
	""" Enable or disable the automatic checkpoints """
	...

def setBinding(*args: _Any) -> _Any:
	""" The setBinding command updates the binding configuration for a specified policy type and scope. Use this command to add a server-specific binding, update an attachment to use a custom binding, edit binding attributes, or remove a binding. """
	...

def setCheckpointLocation(*args: _Any) -> _Any:
	""" Set the directory path where the checkpoints are stored """
	...

def setClientDynamicPolicyControl(*args: _Any) -> _Any:
	""" The setClientDynamicPolicyControl command sets the WSPolicy client acquisition information for a specified resource within an application. """
	...

def setCompUnitTargetAutoStart(*args: _Any) -> _Any:
	""" Enable or disable "autostart" """
	...

def setDefaultBindings(*args: _Any) -> _Any:
	""" The setDefaultBindings command updates the default binding names for a specified domain or server. """
	...

def setDefaultContextService(*args: _Any) -> _Any:
	""" Set the JNDI name that is bound to java:comp/DefaultContextService. """
	...

def setDefaultDataSource(*args: _Any) -> _Any:
	""" Set the JNDI name that is bound to java:comp/DefaultDataSource. """
	...

def setDefaultJMSConnectionFactory(*args: _Any) -> _Any:
	""" Set the JNDI name that is bound to java:comp/DefaultJMSConnectionFactory. """
	...

def setDefaultManagedExecutor(*args: _Any) -> _Any:
	""" Set the JNDI name that is bound to java:comp/DefaultManagedExecutorService. """
	...

def setDefaultManagedScheduledExecutor(*args: _Any) -> _Any:
	""" Set the JNDI name that is bound to java:comp/DefaultManagedScheduledExecutorService. """
	...

def setDefaultManagedThreadFactory(*args: _Any) -> _Any:
	""" Set the JNDI name that is bound to java:comp/DefaultManagedThreadFactory. """
	...

def setDefaultSIBWSOutboundPort(*args: _Any) -> _Any:
	""" Set the default outbound port for an outbound service. """
	...

def setDefaultTraceRuleForIntelligentManagement(*args: _Any) -> _Any:
	""" Set default trace for Intelligent Management """
	...

def setDynamicClusterMaxInstances(*args: _Any) -> _Any:
	""" Set dynamic cluster maximum number of cluster instances """
	...

def setDynamicClusterMaxNodes(*args: _Any) -> _Any:
	""" Set dynamic cluster maximum number of cluster nodes """
	...

def setDynamicClusterMembershipPolicy(*args: _Any) -> _Any:
	""" Set dynamic cluster membership policy """
	...

def setDynamicClusterMinInstances(*args: _Any) -> _Any:
	""" Set dynamic cluster minimum number of cluster instances """
	...

def setDynamicClusterMinNodes(*args: _Any) -> _Any:
	""" Set dynamic cluster minimum number of cluster nodes """
	...

def setDynamicClusterOperationalMode(*args: _Any) -> _Any:
	""" Set dynamic cluster operational mode """
	...

def setDynamicClusterVerticalInstances(*args: _Any) -> _Any:
	""" Set dynamic cluster vertical stacking of instances on node """
	...

def setEmailList(*args: _Any) -> _Any:
	""" Sets the notification email list for the configured audit notification. """
	...

def setGenericJVMArguments(*args: _Any) -> _Any:
	""" Set Java virtual machine (JVM) Generic JVM Arguments Size """
	...

def setGlobalSecurity(*args: _Any) -> _Any:
	""" The administrative security field in the security.xml file is updated based on the user input of true or false. """
	...

def setIdMgrCustomProperty(*args: _Any) -> _Any:
	""" Sets/adds/deletes custom property to a repository configuration. If value is not specified or an empty string then the property will be deleted from the repository configuration. If name does not exist then it will be added, if a value is specified. If name is "*" then all the custom properties will be deleted. """
	...

def setIdMgrDefaultRealm(*args: _Any) -> _Any:
	""" Sets the name of the default realm. """
	...

def setIdMgrEntryMappingRepository(*args: _Any) -> _Any:
	""" Sets or updates an entry mapping repository configuration. """
	...

def setIdMgrLDAPAttrCache(*args: _Any) -> _Any:
	""" Sets up the LDAP attribute cache configuration. """
	...

def setIdMgrLDAPContextPool(*args: _Any) -> _Any:
	""" Sets up the LDAP context pool configuration. """
	...

def setIdMgrLDAPGroupConfig(*args: _Any) -> _Any:
	""" Sets up the LDAP group configuration. """
	...

def setIdMgrLDAPSearchResultCache(*args: _Any) -> _Any:
	""" Sets up the LDAP search result cache configuration. """
	...

def setIdMgrPropertyExtensionRepository(*args: _Any) -> _Any:
	""" Sets or updates the property mapping repository configuration. """
	...

def setIdMgrRealmDefaultParent(*args: _Any) -> _Any:
	""" Sets the default parent of an entity type in a specified realm. If mapping does not exist it is added, else the mapping is updated. If realm name is not specified, default realm is used. """
	...

def setIdMgrRealmURAttrMapping(*args: _Any) -> _Any:
	""" Sets the user registry user or group attribute mapping for a realm. """
	...

def setIdMgrUseGlobalSchemaForModel(*args: _Any) -> _Any:
	""" Sets the global schema option for the data model in a multiple security domain environment, where global schema refers to the schema of the admin domain. """
	...

def setInheritDefaultsForDestination(*args: _Any) -> _Any:
	""" Allows the override for inheritance for an individual destination.  Setting the "inherit" value to true will allow the destination to inherit from the default values. """
	...

def setInheritReceiverForTopic(*args: _Any) -> _Any:
	""" Allows the override for receiver inheritance for an individual topic on a specified topic space.  Setting the "inherit" value to true will allow the topic to inherit from the default values. """
	...

def setInheritSenderForTopic(*args: _Any) -> _Any:
	""" Allows the override for sender inheritance for an individual topic on a specified topic space.  Setting the "inherit" value to true will allow the topic to inherit from the default values. """
	...

def setJVMDebugMode(*args: _Any) -> _Any:
	""" Set Java virtual machine (JVM) Debug Mode """
	...

def setJVMInitialHeapSize(*args: _Any) -> _Any:
	""" Set Java virtual machine (JVM) Initial Heap Size """
	...

def setJVMMaxHeapSize(*args: _Any) -> _Any:
	""" Set Java virtual machine (JVM) Maximum Heap Size """
	...

def setJVMMode(*args: _Any) -> _Any:
	""" Set the JVM mode to either 64-bit or 31-bit for a release prior to V9. Starting from V9, only 64-bit is supported. """
	...

def setJVMProperties(*args: _Any) -> _Any:
	""" Set Java virtual machine (JVM) configuration for the application server. """
	...

def setJVMSystemProperties(*args: _Any) -> _Any:
	""" set Java virtual machine (JVM) system property for the application server's process. """
	...

def setLTPATimeout(*args: _Any) -> _Any:
	""" Set the LTPA authentication mechanism timeout from global security or an application security domain. """
	...

def setMaintenanceMode(*args: _Any) -> _Any:
	""" sets maintenance mode indicator on specified server """
	...

def setNodeDefaultSDK(*args: _Any) -> _Any:
	""" Set the default SDK by name or by location for the node """
	...

def setPolicyType(*args: _Any) -> _Any:
	""" The setPolicyType command updates the attributes of a specified policy. """
	...

def setPolicyTypeAttribute(*args: _Any) -> _Any:
	""" The setPolicyTypeAttribute command sets an attribute for a specific policy. """
	...

def setPreference(*args: _Any) -> _Any:
	""" Command to set a user preference """
	...

def setProcessDefinition(*args: _Any) -> _Any:
	""" Set the process definition of an application server. """
	...

def setProviderPolicySharingInfo(*args: _Any) -> _Any:
	""" The setProviderPolicySharingInfo command sets the WSPolicy provider sharing information for a specified resource within an application. """
	...

def setResourceProperty(*args: _Any) -> _Any:
	""" This command sets the value of a specified property defined on a resource provider such as JDBCProvider or a connection factory such as DataSource or JMSConnectionFactory. If the property with specified key is defined already, then this command overrides the value. If none property with specified key is defined yet, then this command will add the property with specified key and value. """
	...

def setRuntimeRegistrationProperties(*args: _Any) -> _Any:
	""" Set certain runtime properties for devices and job managers. Caution: a null ID implies each and everyone """
	...

def setSAMLIssuerConfigInBinding(*args: _Any) -> _Any:
	""" Set SAML Issuer Configuration in the specified bindings as custom properties """
	...

def setSendEmail(*args: _Any) -> _Any:
	""" Sets the option to send an audit notification email. """
	...

def setServerInstance(*args: _Any) -> _Any:
	""" Set Server Instance configuration. This command only applies to the z/OS platform. """
	...

def setServerSDK(*args: _Any) -> _Any:
	""" Set server SDK by name or by location """
	...

def setServerSecurityLevel(*args: _Any) -> _Any:
	""" Configure the security level for a secure proxy or management server. """
	...

def setTemplateProperty(*args: _Any) -> _Any:
	""" Set a property in server template's metadata. Use this command with caution. Changing a template metadata property incorrectly will result in new server creation failure. """
	...

def setTraceSpecification(*args: _Any) -> _Any:
	""" Set the trace specification for the server. If the server is running new trace specification takes effect immediately. This command also saves the trace specification in configuration. """
	...

def setUseRegistryServerId(*args: _Any) -> _Any:
	""" The useRegistryServerId security field in userRegistry object in the security.xml file is updated based on the user input of true or false. """
	...

def setVariable(*args: _Any) -> _Any:
	""" Set the value for a variable. A variable is a configuration property that can be used to provide a parameter for some values in the system. """
	...

def setWebServerRoutingRulesProperty(*args: _Any) -> _Any:
	""" Use this command to set properties associated with routing rules. """
	...

def setupIdMgrDBTables(*args: _Any) -> _Any:
	""" Creates and populates tables for database in virtual member manager. """
	...

def setupIdMgrEntryMappingRepositoryTables(*args: _Any) -> _Any:
	""" Creates and populates tables for entry mapping database in virtual member manager. """
	...

def setupIdMgrPropertyExtensionRepositoryTables(*args: _Any) -> _Any:
	""" Creates and populates tables for a property extension database in virtual member manager. """
	...

def showAuditLogEncryptionInfo(*args: _Any) -> _Any:
	""" Displays information about the keystore used during Audit Record encryption """
	...

def showExternalBundleRepository(*args: _Any) -> _Any:
	""" Shows the configured parameters of the named external bundle repository. """
	...

def showIdMgrConfig(*args: _Any) -> _Any:
	""" Shows the current configuration with unsaved changes. """
	...

def showJAXWSHandler(*args: _Any) -> _Any:
	""" Show the attributes of a JAX-WS Handler """
	...

def showJAXWSHandlerList(*args: _Any) -> _Any:
	""" Show the attributes of a JAX-WS Handler _List """
	...

def showJPASpecLevel(*args: _Any) -> _Any:
	""" Displays the active JPA specification level for a Server or ServerCluster.The operation requires either an ObjectName referencing the target object, or parameters identifying the target node and server. """
	...

def showJVMProperties(*args: _Any) -> _Any:
	""" List Java virtual machine (JVM) configuration for the application server's process. """
	...

def showJVMSystemProperties(*args: _Any) -> _Any:
	""" Show Java virtual machine (JVM) system properties for the application server.'s process. """
	...

def showJaxrsProvider(*args: _Any) -> _Any:
	""" Displays the active JAXRS Provider for a Server or ServerCluster.The operation requires either an ObjectName referencing the target object, or parameters identifying the target node and server. """
	...

def showJobSchedulerAttributes(*args: _Any) -> _Any:
	""" list all job scheduler attributes """
	...

def showLMService(*args: _Any) -> _Any:
	""" Use the "showLMService" command to show the attributes of a local mapping service. """
	...

def showLocalRepositoryBundle(*args: _Any) -> _Any:
	""" Shows the information about a bundle in the internal bundle repository. """
	...

def showLongRunningSchedulerAttributes(*args: _Any) -> _Any:
	""" (Deprecated) list all long-running scheduler attributes. Use showJobSchedulerAttributes. """
	...

def showMiddlewareApp(*args: _Any) -> _Any:
	""" Use this command to show the attributes of a middleware application. """
	...

def showMiddlewareDescriptorInformation(*args: _Any) -> _Any:
	""" Use this command to display the contents of the specified middleware descriptor """
	...

def showMiddlewareServerInfo(*args: _Any) -> _Any:
	""" Use this command to show information on the middleware server """
	...

def showProcessDefinition(*args: _Any) -> _Any:
	""" Show the process definition of the server """
	...

def showResourceProperties(*args: _Any) -> _Any:
	""" This command list all the property values defined on a resource provider such as JDBCProvider or a connection factory such as DataSource or JMSConnectionFactory. """
	...

def showSAMLIdpPartner(*args: _Any) -> _Any:
	""" This command displays the SAML TAI IdP partner in the security configuration. If an idpId is not specified, all the SAML TAI IdP partners are displayed. """
	...

def showSAMLTAISSO(*args: _Any) -> _Any:
	""" This command displays the SAML TAI SSO in the security configuration. If an ssoId is not specified, all the SAML TAI SSO service providers are displayed. """
	...

def showSIBDestination(*args: _Any) -> _Any:
	""" Show a bus destination's attributes. """
	...

def showSIBEngine(*args: _Any) -> _Any:
	""" Show a messaging engine's attributes. """
	...

def showSIBForeignBus(*args: _Any) -> _Any:
	""" Show detail for a SIB foreign bus. """
	...

def showSIBJMSActivationSpec(*args: _Any) -> _Any:
	""" Show the attributes of target SIB JMS activation specification. """
	...

def showSIBJMSConnectionFactory(*args: _Any) -> _Any:
	""" Return a list containing the SIB JMS connection factory's attribute names and values. """
	...

def showSIBJMSQueue(*args: _Any) -> _Any:
	""" Return a list containing the SIB JMS queue's attribute names and values. """
	...

def showSIBJMSTopic(*args: _Any) -> _Any:
	""" Return a list containing the SIB JMS topic's attribute names and values. """
	...

def showSIBLink(*args: _Any) -> _Any:
	""" Show detail for a SIB link. """
	...

def showSIBMQLink(*args: _Any) -> _Any:
	""" Show detail for a WebSphere MQ link. """
	...

def showSIBMediation(*args: _Any) -> _Any:
	""" Show the attributes of a mediation. """
	...

def showSIBWMQServer(*args: _Any) -> _Any:
	""" Display a named WebSphere MQ server's attributes. """
	...

def showSIBWMQServerBusMember(*args: _Any) -> _Any:
	""" Display a named WebSphere MQ server bus members attributes. """
	...

def showSIBus(*args: _Any) -> _Any:
	""" Show the attributes of a bus. """
	...

def showSIBusMember(*args: _Any) -> _Any:
	""" Show a member from a bus. """
	...

def showServerInfo(*args: _Any) -> _Any:
	""" show detailed information of a specified server. """
	...

def showServerInstance(*args: _Any) -> _Any:
	""" Show Server Instance configuration. This command only applies to the z/OS platform. """
	...

def showServerTypeInfo(*args: _Any) -> _Any:
	""" Show server type information. """
	...

def showServiceMap(*args: _Any) -> _Any:
	""" Use the "showServiceMap" command to show the attributes of a service map. """
	...

def showSpnego(*args: _Any) -> _Any:
	""" This command displays the SPNEGO Web authentication in the security configuration. """
	...

def showSpnegoFilter(*args: _Any) -> _Any:
	""" This command displays the SPNEGO Web authentication Filter in the security configuration. If a host name is not specified, all the SPNEGO Web authentication Filters are displayed. """
	...

def showSpnegoTAIProperties(*args: _Any) -> _Any:
	""" This command displays the SPNEGO TAI properties in the security configuration. If an spnId is not specified, all the SPNEGO TAI properties are displayed. """
	...

def showTemplateInfo(*args: _Any) -> _Any:
	""" A command that displays all the Metadata about a given template. """
	...

def showVariables(*args: _Any) -> _Any:
	""" List variable values under a scope. """
	...

def showWMQ(*args: _Any) -> _Any:
	""" Shows all IBM MQ resource adapter and IBM MQ messaging provider settings which can be set by the manageWMQ command. """
	...

def showWMQActivationSpec(*args: _Any) -> _Any:
	""" Shows the attributes of the IBM MQ Activation Specification provided to the command. """
	...

def showWMQConnectionFactory(*args: _Any) -> _Any:
	""" Shows the attributes of the IBM MQ Connection Factory provided to the command. """
	...

def showWMQQueue(*args: _Any) -> _Any:
	""" Shows the attributes of the IBM MQ Queue provided to the command. """
	...

def showWMQTopic(*args: _Any) -> _Any:
	""" Shows the attributes of the IBM MQ Topic provided to the command. """
	...

def showWSNAdministeredSubscriber(*args: _Any) -> _Any:
	""" Show the properties of a WSNAdministeredSubscriber object in a human readable form. """
	...

def showWSNService(*args: _Any) -> _Any:
	""" Show the properties of a WSNService object in a human readable form. """
	...

def showWSNServicePoint(*args: _Any) -> _Any:
	""" Show the properties of a WSNServicePoint object in a human readable form. """
	...

def showWSNTopicDocument(*args: _Any) -> _Any:
	""" Show the properties of a WSNTopicDocument in a human readable form. """
	...

def showWSNTopicNamespace(*args: _Any) -> _Any:
	""" Show the properties of a WSNTopicNamespace object in a human readable form. """
	...

def startBLA(*args: _Any) -> _Any:
	""" Start all composition units of a specified business-level application. """
	...

def startCertificateExpMonitor(*args: _Any) -> _Any:
	""" Start the Certificate Expiration Monitor. """
	...

def startLMService(*args: _Any) -> _Any:
	""" Use the "startLMService" command to start a stopped local mapping service. """
	...

def startMiddlewareServer(*args: _Any) -> _Any:
	""" Use this command to start a middleware server """
	...

def startPollingJobManager(*args: _Any) -> _Any:
	""" Start a managed node's polling against a JobManager, possibly after a certain delay """
	...

def startWasCEApp(*args: _Any) -> _Any:
	""" Use this command to start a WAS CE application. """
	...

def stopBLA(*args: _Any) -> _Any:
	""" Stop all composition units of a specified business-level application. """
	...

def stopLMService(*args: _Any) -> _Any:
	""" Use the "stopLMService" command to stop a started local mapping service. """
	...

def stopMiddlewareServer(*args: _Any) -> _Any:
	""" Use this command to stop a middleware server """
	...

def stopPollingJobManager(*args: _Any) -> _Any:
	""" Stop a managed node's polling against a JobManager """
	...

def stopWasCEApp(*args: _Any) -> _Any:
	""" Use this command to stop a WAS CE application. """
	...

def submitJob(*args: _Any) -> _Any:
	""" Submits a new job for execution. """
	...

def suspendJob(*args: _Any) -> _Any:
	""" Suspends a previously submitted job. """
	...

def testDynamicClusterMembershipPolicy(*args: _Any) -> _Any:
	""" Test the dynamic cluster membership policy to see what nodes will be returned """
	...

def transferAttachmentsForPolicySet(*args: _Any) -> _Any:
	""" The transferAttachmentsForPolicySet command transfers all attachments from one policy set to another policy set. """
	...

def unassignSTSEndpointTokenType(*args: _Any) -> _Any:
	""" Disassociate an endpoint from its token type. """
	...

def unconfigureAuthzConfig(*args: _Any) -> _Any:
	""" Removes the external JAAC authorization provider """
	...

def unconfigureCSIInbound(*args: _Any) -> _Any:
	""" Removes CSI inbound information from an application security domain. """
	...

def unconfigureCSIOutbound(*args: _Any) -> _Any:
	""" Removes CSI outbound information from an application security domain. """
	...

def unconfigureInterceptor(*args: _Any) -> _Any:
	""" Removes an interceptor from global security configuration or from a security domain. """
	...

def unconfigureJAASLogin(*args: _Any) -> _Any:
	""" Unconfigures a JAAS login in an application security domain.  This removes the JAAS login object and all it's entries. """
	...

def unconfigureJAASLoginEntry(*args: _Any) -> _Any:
	""" Unconfigures a JAAS login entry in the administrative security configuration or in an application security domain.  Note: note all JAAS login entries can be removed. """
	...

def unconfigureJaspi(*args: _Any) -> _Any:
	""" Removes the Jaspi configuration from a security domain. """
	...

def unconfigureLoginModule(*args: _Any) -> _Any:
	""" Unconfigures a login module from a login entry in the administrative security configuration or in an application security domain. """
	...

def unconfigureSpnego(*args: _Any) -> _Any:
	""" This command unconfigures SPNEGO Web authentication in the security configuration. """
	...

def unconfigureTAM(*args: _Any) -> _Any:
	""" This command unconfigures embedded Tivoli Access Manager on the WebSphere Application Server node or nodes specified. """
	...

def unconfigureTAMTAI(*args: _Any) -> _Any:
	""" This command unconfigures the embedded Tivoli Access Manager Trust Association Interceptor with classname TAMTrustAsociationInterceptorPlus. This task does not include removing any custom properties from the security configuration """
	...

def unconfigureTAMTAIPdjrte(*args: _Any) -> _Any:
	""" This command performs the tasks necessary to unconfigure the Tivoli Access Manager Runtime for Java. The specific tasks run are PDJrteCfg and SvrSslCfg. """
	...

def unconfigureTAMTAIProperties(*args: _Any) -> _Any:
	""" This command removes the custom properties from the security configuration for the embedded Tivoli Access Manager Trust Association Interceptor with classname TAMTrustAsociationInterceptorPlus. """
	...

def unconfigureTrustAssociation(*args: _Any) -> _Any:
	""" Removes the trust association object from a security domain. """
	...

def unconfigureTrustedRealms(*args: _Any) -> _Any:
	""" Unconfigures an inbound or outbound trusted realms by removing the realm object from the configuration. """
	...

def unconfigureUserRegistry(*args: _Any) -> _Any:
	""" Unconfigure a user registry in the administrative security configuration or an application security domain. """
	...

def undeployWasCEApp(*args: _Any) -> _Any:
	""" Use this command to undeploy a WAS CE application from a server. """
	...

def uninstallMiddlewareApp(*args: _Any) -> _Any:
	""" Use this command to uninstall a middleware application. """
	...

def uninstallServiceMap(*args: _Any) -> _Any:
	""" Use the "uninstallServiceMap" command to uninstall a service map. """
	...

def unmediateSIBDestination(*args: _Any) -> _Any:
	""" Mediate a destination. """
	...

def unpublishSIBWSInboundService(*args: _Any) -> _Any:
	""" Unpublish an inbound service from a UDDI registry. """
	...

def unregisterApp(*args: _Any) -> _Any:
	""" Use this command to unregister a middleware application. """
	...

def unregisterHost(*args: _Any) -> _Any:
	""" Unregister a host from the job manager. """
	...

def unregisterWithJobManager(*args: _Any) -> _Any:
	""" Unregister a managed node from a JobManager """
	...

def unsetAppActiveSecuritySettings(*args: _Any) -> _Any:
	""" Unsets active security settings on a security domain.  The attribute is removed from the security domain configuration. """
	...

def unsetMaintenanceMode(*args: _Any) -> _Any:
	""" unsets maintenance mode indicator on specified server """
	...

def updateARSConfig(*args: _Any) -> _Any:
	""" Updates the installation/deployment of the Asynchronous Response Servlet which is used when JAX-WS client applications use the JAX-WS asynchronous API """
	...

def updateAppOnCluster(*args: _Any) -> _Any:
	""" Updates all cluster members about the application config changes. """
	...

def updateAsset(*args: _Any) -> _Any:
	""" Update an imported asset file. """
	...

def updateCluster(*args: _Any) -> _Any:
	""" Updates the configuration of an application server cluster. """
	...

def updateClusterMemberWeights(*args: _Any) -> _Any:
	""" Updates the weights of the specified cluster members. """
	...

def updateDistributedCacheProperty(*args: _Any) -> _Any:
	""" updateSeveralWSSDistributedCacheConfigCmdDesc """
	...

def updateGroup(*args: _Any) -> _Any:
	""" Updates the attributes of a group. """
	...

def updateIdMgrDBRepository(*args: _Any) -> _Any:
	""" Updates a database repository configuration. """
	...

def updateIdMgrFileRepository(*args: _Any) -> _Any:
	""" Updates a file repository configuration. """
	...

def updateIdMgrLDAPAttrCache(*args: _Any) -> _Any:
	""" Updates the LDAP attribute cache configuration. """
	...

def updateIdMgrLDAPBindInfo(*args: _Any) -> _Any:
	""" Dynamically updates the LDAP server bind information. If bindDN is specified bindPassword must be specified. If only id is specified then LDAP server information is refreshed. """
	...

def updateIdMgrLDAPContextPool(*args: _Any) -> _Any:
	""" Updates the LDAP context pool configuration. """
	...

def updateIdMgrLDAPEntityType(*args: _Any) -> _Any:
	""" Updates an existing LDAP entity type definition to an LDAP repository configuration. This command can be used to add more values to multivalued parameters. """
	...

def updateIdMgrLDAPGroupDynamicMemberAttr(*args: _Any) -> _Any:
	""" Updates a dynamic member attribute configuration of an LDAP group configuration. """
	...

def updateIdMgrLDAPGroupMemberAttr(*args: _Any) -> _Any:
	""" Updates a member attribute configuration of an LDAP group configuration. """
	...

def updateIdMgrLDAPRepository(*args: _Any) -> _Any:
	""" Updates an LDAP repository configuration. """
	...

def updateIdMgrLDAPSearchResultCache(*args: _Any) -> _Any:
	""" Updates the LDAP search result cache configuration. """
	...

def updateIdMgrLDAPServer(*args: _Any) -> _Any:
	""" Updates an LDAP server configuration of the LDAP repository configuration. """
	...

def updateIdMgrRealm(*args: _Any) -> _Any:
	""" Updates the configuration of the specified realm. """
	...

def updateIdMgrRepository(*args: _Any) -> _Any:
	""" Updates the configuration of the specified repository. To add multiple values to a multivalued parameter, call this command repeatedly. """
	...

def updateIdMgrRepositoryBaseEntry(*args: _Any) -> _Any:
	""" Updates a base entry for the specified repository. """
	...

def updateIdMgrSupportedEntityType(*args: _Any) -> _Any:
	""" Updates a supported entity type configuration. """
	...

def updateLMService(*args: _Any) -> _Any:
	""" Use the "updateLMService" command to update details about an existing local mapping service. """
	...

def updatePolicySet(*args: _Any) -> _Any:
	""" The updatePolicySet command enables you to input an attribute list to update the policy set. You can use this command to update all attributes for the policy set, or a subset of attributes. """
	...

def updatePolicySetAttachment(*args: _Any) -> _Any:
	""" The updatePolicySetAttachment command updates the resources that apply to a policy set attachment. """
	...

def updateRAR(*args: _Any) -> _Any:
	""" Update an existing resource adapter with the supplied RAR file and configure any new properties that exist on deployed objects within the resource adapter to be updated. 
    
    Before using the updateRAR command, use the compareResourceAdapterToRAR command to verify the RAR is compatible for upgrading the resource adapter, and use the findOtherRAsToUpdate command to determine the set of resources adapters that need be updated using the supplied RAR.
    """
	...

def updateSAMLIssuerConfig(*args: _Any) -> _Any:
	""" Update SAML Issuer Configuration data """
	...

def updateSCClientCacheConfiguration(*args: _Any) -> _Any:
	""" Update the SC cache configuration """
	...

def updateSCClientCacheCustomConfiguration(*args: _Any) -> _Any:
	""" Update the SC custom config """
	...

def updateSTSEndpointTokenType(*args: _Any) -> _Any:
	""" Update the assigned token type for an endpoint. If the local name parameter is omitted, the default token type is assumed. """
	...

def updateSTSTokenTypeConfiguration(*args: _Any) -> _Any:
	""" Update the configuration for an existing token type. Token type URIs must be unique. """
	...

def updateUser(*args: _Any) -> _Any:
	""" Updates the attributes of a user. """
	...

def updateWSSDistributedCacheConfig(*args: _Any) -> _Any:
	""" Update Web Services Security Distrubuted Cache configuration properties """
	...

def updateWSSDistributedCacheCustomConfig(*args: _Any) -> _Any:
	""" Update Web Services Security distributed cache configuration custom properties """
	...

def upgradeBindings(*args: _Any) -> _Any:
	""" The upgradeBindings command upgrades bindings of an older version to the current version. """
	...

def validateAdminName(*args: _Any) -> _Any:
	""" Validates the existence of the administrator name in the input user registry. """
	...

def validateConfigProperties(*args: _Any) -> _Any:
	""" Validate configuration properties in properites file """
	...

def validateEdition(*args: _Any) -> _Any:
	""" Prepares an edition for VALIDATION. """
	...

def validateKrbConfig(*args: _Any) -> _Any:
	""" Validates the Kerberos configuration data either in the global security configuration file security.xml or specified as an input parameters. """
	...

def validateLDAPConnection(*args: _Any) -> _Any:
	""" Validates the connection to the specified LDAP server. """
	...

def validatePolicySet(*args: _Any) -> _Any:
	""" The validatePolicySet command validates the policies in the policy set. """
	...

def validateSpnegoConfig(*args: _Any) -> _Any:
	""" Validates the SPNEGO Web authentication configuration. """
	...

def viewAsset(*args: _Any) -> _Any:
	""" View options for a specified asset. """
	...

def viewBLA(*args: _Any) -> _Any:
	""" View options for a specified business-level application. """
	...

def viewCompUnit(*args: _Any) -> _Any:
	""" View options for specified a composition unit of a business-level application. """
	...

