import neovim

@neovim.plugin
class TestPlugin:
    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.function("TestFunction", sync=True)
    def test_function(self, args):
        return 3

    @neovim.command("TestCommand", range='', nargs='*')
    def test_command(self, args, rng):
        self.nvim.current.line = ('Hello with args: {}, range: {}'.format(args, rng))

    @neovim.autocmd('BufEnter', pattern='*.py', eval='expand("<afile>")', sync=True)
    def on_bufenter(self, filename):
        self.nvim.out_write("testplugin is in {} \n".format(filename))


