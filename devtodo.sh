TODO_OPTIONS="--timeout --summary"

cd()
{
	if builtin cd "$@"; then
		devtodo ${TODO_OPTIONS}
	fi
}

pushd()
{
	if builtin pushd "$@"; then
		devtodo ${TODO_OPTIONS}
	fi
}

popd()
{
	if builtin popd "$@"; then
		devtodo ${TODO_OPTIONS}
	fi
}

# Run todo initially upon login
devtodo ${TODO_OPTIONS}

