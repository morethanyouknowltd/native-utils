const { MainWindow } = require('bindings')('nativeutils')

export function displays() {
  const mainDisplay = MainWindow.getMainScreen()
  return [mainDisplay]
}
