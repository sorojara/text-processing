import click
from mine_dwarf.core import read_file
from mine_dwarf.title import generate_random_title

@click.group()
@click.pass_context
def cli(ctx):
	ctx.obj={}
	subcommand = ctx.invoked_subcommand
	print(generate_random_title())


@cli.command('print-file')
@click.option('--file', help="File to open", default="")
def file_read(file):
    """This is an example script to learn Click."""
    read_file(file)

def run_main():
	cli(auto_envvar_prefix='dwarf')

if __name__ == '__main__':
	run_main()
