# Generate DNS zone from YAML
Purpose is to generate DNS zone lines compatible with [cli53](https://github.com/barnybug/cli53) for import into Route53.

# Example
```
# ./dns-zone-from-yaml.py example.yaml
host2 A 192.0.2.3
host1 A 192.0.2.1
web CNAME host1.example.com
```

# Run with Docker
```
docker run -v "$PWD:/input" --rm tomologic/dns-yaml /input/example.yaml
```
