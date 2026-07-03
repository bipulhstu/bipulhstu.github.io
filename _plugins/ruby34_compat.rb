# Local-build compatibility shim.
#
# Jekyll 3.9 / Liquid 4.0.3 (pinned by the github-pages gem) still call the
# taint API (String#tainted?, Object#taint/untaint), which was removed in
# Ruby 3.2+. Running the site locally on a modern Ruby (3.4/4.0) therefore
# crashes with "undefined method 'tainted?'". These no-op definitions restore
# just enough of the old API for the local build to succeed.
#
# This file only runs during local `jekyll build/serve`. GitHub Pages builds
# the site with its own (compatible) Ruby and ignores custom _plugins, so this
# shim has no effect on deployment.
unless "".respond_to?(:tainted?)
  class Object
    def tainted?
      false
    end

    def taint
      self
    end

    def untaint
      self
    end
  end
end
