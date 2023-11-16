# ClickCommand start the main script like this.
# bash -ex main.sh

# Every ClickCommand generated env will be prefixed with 'CLICK_' to avoid mixing with sys envs.
name="${CLICK_NAME}"
upper_name=$(printf "${CLICK_NAME}" | tr '[a-z]' '[A-Z]')

# true or false
flag_upper="${CLICK_UPPER}"

if [ $flag_upper == true ]; then
  echo "Hello, ${upper_name}!"
elif [ $flag_upper == false ]; then
  echo "Hello, ${name}!"
else
  echo "should never reach here"
  exit 1
fi
