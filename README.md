# ABC Technologies - Corporate Website (DevOps Assignment 2)

Static corporate website (Home, About Us, Services, Careers, Gallery, Contact Us)
deployed via a full DevOps pipeline: GitHub -> Jenkins -> Docker -> Kubernetes,
with Nagios, Graphite, and Grafana for continuous monitoring.

## Folder structure
```
.
├── src/                  # Website source (HTML, CSS, JS)
├── Dockerfile            # Builds nginx image serving the site
├── nginx.conf            # Custom nginx config (/health, /nginx_status)
├── Jenkinsfile           # CI/CD pipeline definition
├── k8s/
│   ├── deployment.yaml   # Kubernetes Deployment
│   └── service.yaml      # Kubernetes Service (NodePort 30080)
└── monitoring/
    ├── docker-compose.yml         # Nagios + Graphite + Grafana stack
    ├── metrics-collector.py       # Sends CPU/Mem/Network/HTTP metrics to Graphite
    ├── nagios/conf.d/abc_website.cfg
    └── grafana/provisioning/...   # Auto-provisioned datasource + dashboard
```

See the accompanying step-by-step guide for full setup instructions.
