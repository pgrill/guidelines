module SCSSLint
  class Linter::NoPointerEvents < Linter
    include LinterRegistry

    def visit_prop(node)
      if node.name.first.to_s == 'pointer-events'
        add_lint(node, 'IE doesnt support pointer-events.')
      end
    end
  end
end
