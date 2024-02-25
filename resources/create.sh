#!/bin/bash

# Define the package name
package="resources"

# Define the resource commands
declare -A resource_commands=(
    ["acm.certificate"]="acm delete-certificate --certificate-arn"
    ["athena.workgroup"]="athena delete-work-group --work-group"
    ["backup.recoverypoint"]="backup delete-recovery-point --recovery-point-arn"
    ["cloudformation.stack"]="cloudformation delete-stack --stack-name"
    ["cloudformation.stackset"]="cloudformation delete-stack-set --stack-set-name"
    ["cloudfront.distribution"]="cloudfront delete-distribution --id"
    ["cloudtrail.trail"]="cloudtrail delete-trail --name"
    ["codebuild.project"]="codebuild delete-project --name"
    ["dynamodb.table"]="dynamodb delete-table --table-name"
    ["cloudwatch.alarm"]="cloudwatch delete-alarms --alarm-names"
    ["ecs.cluster"]="ecs delete-cluster --cluster"
    ["ecs.service"]="ecs delete-service --service"
    ["ecs.task"]="ecs stop-task --task"
    ["ecs.taskdefinition"]="ecs deregister-task-definition --task-definition"
    ["ecs.addon"]="ecs delete-addon --addon-name"
    ["ec2.instance"]="ec2 terminate-instances --instance-ids"
    ["ec2.volume"]="ec2 delete-volume --volume-id"
    ["ec2.securitygroup"]="ec2 delete-security-group --group-id"
    ["ec2.subnet"]="ec2 delete-subnet --subnet-id"
    ["ec2.internetgateway"]="ec2 delete-internet-gateway --internet-gateway-id"
    ["ec2.launchtemplate"]="ec2 delete-launch-template --launch-template-id"
    ["ec2.routetable"]="ec2 delete-route-table --route-table-id"
    ["ec2.vpc"]="ec2 delete-vpc --vpc-id"
    ["ec2.transitgateway"]="ec2 delete-transit-gateway --transit-gateway-id"
    ["ec2.transitgateway-attachment"]="ec2 delete-transit-gateway-attachment --transit-gateway-attachment-id"
    ["ec2.networkinterface"]="ec2 delete-network-interface --network-interface-id"
    ["ec2.snapshot"]="ec2 delete-snapshot --snapshot-id"
    ["ec2.keypair"]="ec2 delete-key-pair --key-name"
    ["ec2.image"]="ec2 deregister-image --image-id"
    ["ec2.fleet"]="ec2 delete-fleet --fleet-id"
    ["ec2.elasticip"]="ec2 release-address --allocation-id"
    ["ec2.vpcendpoint"]="ec2 delete-vpc-endpoints --vpc-endpoint-ids"
    ["ec2.vpcpeeringconnection"]="ec2 delete-vpc-peering-connection --vpc-peering-connection-id"
    ["ec2.customergateway"]="ec2 delete-customer-gateway --customer-gateway-id"
    ["ec2.natgateway"]="ec2 delete-nat-gateway --nat-gateway-id"
    ["ec2.networkinsights-path"]="ec2 delete-network-insights-path --network-insights-path-id"
    ["ec2.networkacl"]="ec2 delete-network-acl --network-acl-id"
    ["ec2.vpnconnection"]="ec2 delete-vpn-connection --vpn-connection-id"
    ["ec2.vpngateway"]="ec2 delete-vpn-gateway --vpn-gateway-id"
    ["ecr.repository"]="ecr delete-repository --repository-name"
    ["eks.cluster"]="eks delete-cluster --name"
    ["eks.addon"]="eks delete-addon --cluster-name"
    ["eks.nodegroup"]="eks delete-nodegroup --nodegroup-name --cluster-name"
    ["elasticfilesystem.access-point"]="efs delete-access-point --access-point-id"
    ["elasticfilesystem.file-system"]="efs delete-file-system --file-system-id"
    ["elasticloadbalancing.listener"]="elasticloadbalancing delete-listener --listener-arn"
    ["elasticloadbalancing.listener-rule"]="elasticloadbalancing delete-listener-rule --rule-arn"
    ["elasticloadbalancing.loadbalancer"]="elasticloadbalancing delete-load-balancer --load-balancer-name"
    ["elasticloadbalancing.targetgroup"]="elasticloadbalancing delete-target-group --target-group-arn"
    ["events.rule"]="events delete-rule --name"
    ["glue.crawler"]="glue delete-crawler --name"
    ["iam.oidcprovider"]="iam delete-open-id-connect-provider --open-id-connect-provider-arn"
    ["iam.policy"]="iam delete-policy --policy-arn"
    ["iam.user"]="iam delete-user --user-name"
    ["iam.instance-profile"]="iam delete-instance-profile --instance-profile-name"
    ["inspector.target"]="inspector delete-assessment-target --assessment-target-arn"
    ["kms.key"]="kms delete-key --key-id"
    ["lambda.function"]="lambda delete-function --function-name"
    ["logs.loggroup"]="logs delete-log-group --log-group-name"
    ["payments.payment-instrument"]="payments delete-payment-instrument --id"
    ["rds.db"]="rds delete-db --db-instance-identifier"
    ["rds.dbinstance"]="rds delete-db-instance --db-instance-identifier"
    ["rds.dbsubnetgroup"]="rds delete-db-subnet-group --db-subnet-group-name"
    ["rds.pg"]="rds delete-db-instance --db-instance-identifier"
    ["rds.snapshot"]="rds delete-db-snapshot --db-snapshot-identifier"
    ["rds.subgrp"]="rds delete-db-subnet-group --db-subnet-group-name"
    ["route53.hostedzone"]="route53 delete-hosted-zone --id"
    ["route53.healthcheck"]="route53 delete-health-check --health-check-id"
    ["secretsmanager.secret"]="secretsmanager delete-secret --secret-id"
    ["sns.topic"]="sns delete-topic --topic-arn"
    ["ssm.session"]="ssm terminate-session --session-id"
    ["ssm.document"]="ssm delete-document --name"
    ["servicediscovery.namespace"]="servicediscovery delete-namespace --id"
    ["sqs.queue"]="sqs delete-queue --queue-url"
    ["states.stateMachine"]="stepfunctions delete-state-machine --state-machine-arn"
)

# Loop through each resource command
for resource_command in "${!resource_commands[@]}"; do
    # Split the resource command into package and resource
    IFS='.' read -r -a resource_parts <<< "$resource_command"
    package_name="${resource_parts[0]}"
    resource_name="${resource_parts[1]}"

    # Create the package directory if it doesn't exist
    mkdir -p "$package_name"

    # Create the Python file for the resource
    touch "$package_name/$resource_name.py"
    touch "$package_name/__init__.py"

    # Write the Python class to the file
    echo "from resources.base_resources import BaseArn


class ${resource_name}(BaseArn):
    def __init__(self, arn):
        super().__init__(arn)
        self.deletion_method = \"${resource_commands[$resource_command]}\"
" > "$package_name/$resource_name.py"

    echo "Created ${package_name}/${resource_name}.py"
done

echo "All resources created successfully!"
