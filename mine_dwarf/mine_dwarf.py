import click
import mine_dwarf.core as core
from mine_dwarf.title import generate_random_title

@click.group()
@click.pass_context
def cli(ctx):
	ctx.obj={}
	subcommand = ctx.invoked_subcommand
	print(generate_random_title())

@cli.command('test-me')
@click.option('--file', help="File to open", default="")
@click.option('--wrap-size', help="Text wrapping size", default=40)
def test_me(file, wrap_size):
    """This is an example script to learn Click."""
    core.test_me(file, wrap_size)


@cli.command('print-file')
@click.option('--file', help="File to open", default="")
def file_read(file):
    """This is an example script to learn Click."""
    read_file(file)

def run_main():
	cli(auto_envvar_prefix='dwarf')

if __name__ == '__main__':
	run_main()
