class make_parser:
    def __init__(self, parser):
        self.parser = parser

    def parse_args(self):
        self.parser.add_argument("--port", type=int, default=80, help="Port to scan (default: 80)")
        return self.parser.parse_args()
