import dns.resolver
import logging

logger = logging.getLogger(__name__)

def check(host, domain):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [host]
    result = resolver.query(domain)
    return result
