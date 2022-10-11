"""Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:"""

result = """
Protocol:            OSPF
Prefix:              10.0.24.0/24
AD/Metric:           110/41
Next-Hop:            10.0.13.3
Last update:         3d18h
Outbound Interface:  FastEthernet0/0
"""

ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

#Solutions:
ospf_route = ospf_route.split()
print(ospf_route)
via  = ospf_route.remove("via")
protocol, network, ad_metric, hop, update, interface = ospf_route
protocol = protocol + "SPF"
hop = hop.strip(",")
update = update.strip(",")


result = """
Protocol: {:>14}
Prefix: {:>24}
AD/Metric: {:>17}
Next-Hop: {:>19}
Last update: {:>12}
Outbound Interface: {}""".format(protocol, network, ad_metric, hop, update, interface)
print(result)