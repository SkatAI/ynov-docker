# S04 content

## Guidelines and Recommendations for Writing Dockerfiles p79

keep the build context as minimal
• Use multi-stage builds
• Skip unwanted packages
• Minimize the number of layers

## CMD vs Entrypoint

excellent exemple

<https://medium.com/@mrdevsecops/dockerfile-cmd-vs-entrypoint-78b219d55df0>

Docker ENTRYPOINT and CMD can have two forms:

    Shell form
    Exec form

The syntax for any command in shell form is:

<instruction> <command>

The syntax for instructions in exec form is:

<instruction> ["executable", "parameter"]

You can write Docker CMD/ENTRYPOINT instructions in both forms:

- CMD echo "Hello World" (shell form)
- CMD ["echo", "Hello World"] (exec form)
- ENTRYPOINT echo "Hello World" (shell form)
- ENTRYPOINT ["echo", "Hello World"] (exec form)

### Multi-Stage Builds (see file)

what is the advantage of multi-stage builds over docker compose
see <https://claude.ai/chat/dfdf46cb-7a51-4f3f-9650-2de92e4ec424>
