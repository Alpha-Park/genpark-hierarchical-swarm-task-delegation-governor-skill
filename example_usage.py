from client import HierarchicalSwarmTaskDelegationGovernorClient

def main():
    client = HierarchicalSwarmTaskDelegationGovernorClient()
    res = client.delegate_swarm_tasks('Build fullstack e-commerce app', ['Frontend_Agent', 'Backend_Agent', 'DBA_Agent'])
    print('Swarm Task Delegation Governor: ' + res['delegation_plan_id'])
    print('Assignments: ' + str(len(res['agent_role_assignments'])) + ' roles | Protocol: ' + res['swarm_consensus_protocol'])
    print('Dashboard URL: ' + res['swarm_telemetry_dashboard_url'])

if __name__ == '__main__':
    main()
