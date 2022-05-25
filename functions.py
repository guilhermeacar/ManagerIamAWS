import boto3
import getpass
import json
iam = boto3.client('iam')

def createGroup():
    accountIdaws = input("AWS Account ID : ")
    # Create group Read Only
    create_group_response = iam.create_group(GroupName = 'ReadOnly')
    print(create_group_response)

    # Create group Admin
    create_group_response = iam.create_group(GroupName = 'Admin')
    print(create_group_response)
    # Create a policy Read Only
    my_managed_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iam:Get*",
                "iam:List*",
                "iam:Generate*"
            ],
            "Resource": "*"
        }
      ]
    }
    response = iam.create_policy(
    PolicyName='ReadOnlyPolicy',
    PolicyDocument=json.dumps(my_managed_policy)
    )
    print(response)

    # Create a policy Write
    my_managed_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                "*"
                ],
                "Resource": "*"
            }
        ]
    }
    response = iam.create_policy(
    PolicyName='WritePolicy',
    PolicyDocument=json.dumps(my_managed_policy)
    )
    print(response)
    # Attaching policy
    response2 = iam.attach_group_policy(
        GroupName='ReadOnly',
        PolicyArn='arn:aws:iam::' + accountIdaws + ':policy/ReadOnlyPolicy'
    )
    print(response2)
    # Attaching policy
    response2 = iam.attach_group_policy(
        GroupName='Admin',
        PolicyArn='arn:aws:iam::' + accountIdaws + ':policy/WritePolicy'
    )
    print(response2)



def createUser():
    username = input("Username: ")
    password = getpass.getpass('Password:')
    group = input("Role(Admin|ReadOnly): ")
    created_user = iam.create_user (
        UserName= username
    )
    response = iam.create_login_profile(
        UserName= username,
        Password= password,
        PasswordResetRequired=True
    )
    if group=="Admin":
        response = iam.add_user_to_group(
            UserName = username,
            GroupName = 'Admin'
        )
    else:
        response = iam.add_user_to_group(
            UserName = username,
            GroupName = 'ReadOnly'
        )
    print(created_user)
    print(response)

def listUsers():
    client = boto3.client('iam')
    users = client.list_users()
    user_list = []
    for key in users['Users']:
        result = {}
        Policies = []
        Groups=[]

        result['userName']=key['UserName']
        List_of_Policies =  client.list_user_policies(UserName=key['UserName'])

        result['Policies'] = List_of_Policies['PolicyNames']

        List_of_Groups =  client.list_groups_for_user(UserName=key['UserName'])

        for Group in List_of_Groups['Groups']:
            Groups.append(Group['GroupName'])
        result['Groups'] = Groups

        List_of_MFA_Devices = client.list_mfa_devices(UserName=key['UserName'])

        if not len(List_of_MFA_Devices['MFADevices']):
            result['isMFADeviceConfigured']=False
        else:
            result['isMFADeviceConfigured']=True
        user_list.append(result)

    for key in user_list:
        print (key)


def disableUsers():
    username = input("Username: ")
    response = iam.delete_login_profile(
        UserName= username
    )
    print(response)
