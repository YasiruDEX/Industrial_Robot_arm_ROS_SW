#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/sandun/ws_moveit/src/srdfdom"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/sandun/ws_moveit/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/sandun/ws_moveit/install/lib/python3/dist-packages:/home/sandun/ws_moveit/build/srdfdom/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/sandun/ws_moveit/build/srdfdom" \
    "/usr/bin/python3" \
    "/home/sandun/ws_moveit/src/srdfdom/setup.py" \
    egg_info --egg-base /home/sandun/ws_moveit/build/srdfdom \
    build --build-base "/home/sandun/ws_moveit/build/srdfdom" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/sandun/ws_moveit/install" --install-scripts="/home/sandun/ws_moveit/install/bin"
