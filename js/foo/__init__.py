import check50
import bond

@check50.check()
def foo_exists():
  """ Function foo exists """

    # Create a JavaScript interface
    i = bond.make_bond("JavaScript")
    # Read foo.js
    with open("foo.js") as f:
        # Evaluate the code in foo.js with node
        i.eval_block(f.read())

        # Check if foo is a function
        if i.eval("typeof(foo) !== 'function'"):
            raise check50.Failure("foo is not defined")
