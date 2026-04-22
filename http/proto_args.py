from nxc.helpers.args import DisplayDefaultsNotNone

def proto_args(parser, parents):
    http_parser = parser.add_parser("http", help="Web discovery and title grabbing (OPSEC friendly)", parents=parents, formatter_class=DisplayDefaultsNotNone)
    http_parser.add_argument("--port", type=int, default=80, help="HTTP port (default: 80)")
    
    hgroup = http_parser.add_argument_group("Web Options", "Options for HTTP discovery")
    hgroup.add_argument("--path", type=str, default="/", help="Path to request (default: /)")
    
    return parser
