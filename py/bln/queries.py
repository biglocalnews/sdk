# FRAGMENTS
fragment_user = '''
id
name
displayName
contactMethod
contactMethod
'''

fragment_user_public = '''
id
name
contactMethod
contactMethod
'''

fragment_group = f'''
id
updatedAt
name
contactMethod
contact
description
userRoles {{
  edges {{
    node {{
      role
      user {{
        {fragment_user_public}
      }}
    }}
  }}
}}
'''

fragment_group_public = '''
id
name
contactMethod
contact
'''

fragment_project = '''
id
updatedAt
name
contactMethod
contact
description
isOpen
userRoles {{
  edges {{
    node {{
      role
      user {{
        {fragment_user_public}
      }}
    }}
  }}
}}
groupRoles {{
  edges {{
    node {{
      role
      group {{
        {fragment_group_public}
      }}
    }}
  }}
}}
effectiveUserRoles {{
  edges {{
    node {{
      role
      user {{
        {fragment_user_public}
      }}
    }}
  }}
}}
files {{
  name
  uri
  updatedAt
}}
'''

fragment_oauth2_client_public = '''
id
name
contactMethod
contact
description
scopes
author {{
    {fragment_user_public}
}}
'''

fragment_oauth2_client_private = f'''
{fragment_oauth2_client_public}
secret
pkceRequired
scopes
redirectUris
defaultRedirectUri
oauth2Codes {{
    edges {{
        node {{
            code
            challenge
            scopes
            user {{
                {fragment_user_public}
            }}
        }}
    }}
}}
oauth2Tokens {{
    edges {{
        node {{
            token
            scopes
            user {{
                {fragment_user_public}
            }}
        }}
    }}
}}
'''

# QUERIES

query_node = f'''
query Node($id: ID!) {{
    node(id: $id) {{
        ... on User {{
            {fragment_user}
        }}
        ... on Group {{
            {fragment_group}
        }}
        ... on Project {{
            {fragment_project}
        }}
        ... on OAuth2Client {{
            {fragment_oauth2_client_public}
        }}
    }}
}}

'''

query_everything = f'''
query {{
    user {{
        {fragment_user}
        groupRoles {{
            edges {{
                node {{
                    role
                    group {{
                        {fragment_group}
                    }}
                }}
            }}
        }}
        projectRoles {{
            edges {{
                node {{
                    role
                    project {{
                        {fragment_project}
                    }}
                }}
            }}
        }}
        effectiveProjectRoles {{
            edges {{
                node {{
                    role
                    project {{
                        {fragment_project}
                    }}
                }}
            }}
        }}
        personalTokens {{
            edges {{
                node {{
                    token
                }}
            }}
        }}
        oauth2Codes {{
            edges {{
                node {{
                    scopes
                    client {{
                        {fragment_oauth2_client_public}
                    }}
                }}
            }}
        }}
        oauth2Tokens {{
            edges {{
                node {{
                    scopes
                    client {{
                        {fragment_oauth2_client_public}
                    }}
                }}
            }}
        }}
        oauth2Clients {{
            edges {{
                node {{
                    {fragment_oauth2_client_private}
                }}
            }}
        }}
    }}
}}
'''

query_user = f'''
query {{
    user {{
        {fragment_user}
    }}
}}
'''

query_groupRoles = f'''
query {{
    user {{
        groupRoles {{
            edges {{
                node {{
                    role
                    group {{
                        {fragment_group}
                    }}
                }}
            }}
        }}
    }}
}}
'''

query_projectRoles = f'''
query {{
    user {{
        projectRoles {{
            edges {{
                node {{
                    role
                    project {{
                        {fragment_project}
                    }}
                }}
            }}
        }}
    }}
}}
'''

query_effectiveProjectRoles = f'''
query {{
    user {{
        effectiveProjectRoles {{
            edges {{
                node {{
                    role
                    project {{
                        {fragment_project}
                    }}
                }}
            }}
        }}
    }}
}}
'''

query_personalTokens = '''
query {
    user {
        personalTokens {
            edges {
                node {
                    token
                }
            }
        }
    }
}
'''

query_oauth2Codes = f'''
query {{
    user {{
        oauth2Codes {{
            edges {{
                node {{
                    scopes
                    client {{
                        {fragment_oauth2_client_public}
                    }}
                }}
            }}
        }}
    }}
}}
'''

query_oauth2Tokens = f'''
query {{
    user {{
        oauth2Tokens {{
            edges {{
                node {{
                    scopes
                    client {{
                        {fragment_oauth2_client_public}
                    }}
                }}
            }}
        }}
    }}
}}
'''

query_oauth2Clients = f'''
query {{
    user {{
        oauth2Clients {{
            edges {{
                node {{
                    {fragment_oauth2_client_private}
                }}
            }}
        }}
    }}
}}
'''

query_userNames = '''
query {
    userNames
}
'''

query_groupNames = '''
query {
    groupNames
}
'''

query_openProjects = f'''
query {{
    openProjects {{
        edges {{
            node {{
                {fragment_project}
            }}
        }}
    }}
}}
'''

query_oauth2ClientsPublic = f'''
query {{
    oauth2Cients {{
        {fragment_oauth2_client_public}
    }}
}}
'''

# MUTATIONS

mutation_authorizeOauth2Client = '''
mutation AuthorizeOAuth2Client($input: AuthorizeOAuth2ClientInput!) {{
    authorizeOauth2Client(input: $input) {{
        ok {{
            {fragment_oauth2_client_public}
        }}
        err
    }}
}}
'''

mutation_authorizeWithPkceOauth2Client = '''
mutation AuthorizeWithPKCEOAuth2Client(
    $input: AuthorizeWithPKCEOAuth2ClientInput!
) {{
    authorizeWithPkceOauth2Client(input: $input) {{
        ok {{
            {fragment_oauth2_client_public}
        }}
        err
    }}
}}
'''

mutation_createFileDownloadUri = '''
mutation CreateFileDownloadURI($input: FileURIInput!) {
    createFileDownloadUri(input: $input) {
        ok {
            name
            uri
            uriType
        }
        err
    }
}
'''

mutation_createFileUploadUri = '''
mutation CreateFileUploadURI($input: FileURIInput!) {
    createFileUploadUri(input: $input) {
        ok {
            name
            uri
            uriType
        }
        err
    }
}
'''

mutation_createGroup = f'''
mutation CreateGroup($input: CreateGroupInput!) {{
    createGroup(input: $input) {{
        ok {{
            {fragment_group}
        }}
        err
    }}
}}
'''

mutation_createNewOauth2ClientSecret = f'''
mutation CreateNewOAuth2ClientSecret(
    $input: CreateNewOAuth2ClientSecretInput!
) {{
    createNewOauth2ClientSecret(input: $input) {{
        ok {{
            {fragment_oauth2_client_private}
        }}
        err
    }}
}}
'''

mutation_createOauth2Client = f'''
mutation CreateOAuth2Client($input: CreateOAuth2ClientInput!) {{
    createOauth2Client(input: $input) {{
        ok {{
            {fragment_oauth2_client_private}
        }}
        err
    }}
}}
'''

mutation_createPersonalToken = '''
mutation CreatePersonalToken {
    createPersonalToken {
        ok
        err
    }
}
'''

mutation_createProject = f'''
mutation CreateProject($input: CreateProjectInput!) {{
    createProject(input: $input) {{
        ok {{
            {fragment_project}
        }}
        err
    }}
}}
'''

mutation_deleteFile = '''
mutation DeleteFile($input: FileURIInput!) {
    deleteFile(input: $input) {
        ok {
            name
        }
        err
    }
}
'''

mutation_deleteProject = '''
mutation DeleteProject($input: DeleteProjectInput!) {
    deleteProject(input: $input) {
        ok
        err
    }
}
'''

mutation_deleteOauth2Client = '''
mutation DeleteOAuth2Client($input: DeleteOAuth2ClientInput!) {
    deleteOauth2Client(input: $input) {
        ok
        err
    }
}
'''

mutation_exchangeOauth2CodeForToken = '''
mutation ExchangeOAuth2CodeForToken($input: ExchangeOAuth2CodeForTokenInput!) {
    exchangeOauth2CodeForToken(input: $input) {
        ok
        err
    }
}
'''

mutation_exchangeOauth2CodeWithPkceForToken = '''
mutation ExchangeOAuth2CodeWithPKCEForToken(
    $input: ExchangeOAuth2CodeWithPKCEForTokenInput!
) {
    exchangeOauth2CodeWithPkceForToken(input: $input) {
        ok
        err
    }
}
'''

mutation_revokeOauth2Token = '''
mutation RevokeOAuth2Token($input: RevokeTokenInput!) {
    revokeOauth2Token(input: $input) {
        ok
        err
    }
}
'''

mutation_revokePersonalToken = '''
mutation RevokePersonalToken($input: RevokeTokenInput!) {
    revokePersonalToken(input: $input) {
        ok
        err
    }
}
'''

mutation_unauthorizeOauth2Client = '''
mutation UnauthorizeOAuth2Client (
    $input: UnauthorizeOAuth2ClientInput!
) {
    unauthorizeOauth2Client(input: $input) {
        ok
        err
    }
}
'''

mutation_updateGroup = f'''
mutation UpdateGroup($input: UpdateGroupInput!) {{
    updateGroup(input: $input) {{
        ok {{
            {fragment_group}
        }}
        err
    }}
}}
'''

mutation_updateOauth2Client = f'''
mutation UpdateOAuth2Client($input: UpdateOAuth2ClientInput!) {{
    updateOauth2Client(input: $input) {{
        ok {{
            {fragment_oauth2_client_private}
        }}
        err
    }}
}}
'''

mutation_updateProject = f'''
mutation UpdateProject($input: UpdateProjectInput!) {{
    updateProject(input: $input) {{
        ok {{
            {fragment_project}
        }}
        err
    }}
}}
'''

mutation_updateUser = f'''
mutation UpdateUser($input: UpdateUserInput!) {{
    updateUser(input: $input) {{
        ok {{
            {fragment_user}
        }}
        err
    }}
}}
'''
