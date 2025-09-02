from typing import TYPE_CHECKING

from peakrdl.plugins.exporter import ExporterSubcommandPlugin

from .headergen.exporter import headerGenExporter

if TYPE_CHECKING:
    import argparse
    from systemrdl.node import AddrmapNode


class Exporter(ExporterSubcommandPlugin):
    short_desc = "Export the register model to C/SV header files"


    def add_exporter_arguments(self, arg_group: 'argparse._ActionsContainer') -> None:
        arg_group.add_argument(
            "--language",
            dest="languages",
            choices=["verilog", "c", "cpp"],
            default="verilog",
            help="Target language for header generation. [verilog]"
        )


    def do_export(self, top_node: 'AddrmapNode', options: 'argparse.Namespace') -> None:

        exporter = headerGenExporter(
            languages=options.languages
        )
        exporter.export(
            top_node,
            options.output
        )
