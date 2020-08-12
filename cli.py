import click


@click.group()
# @click.option("--power_on", default = False, help = "Fix Later")
# @click.option("--power_off", default = False, help = "Fix Later")
def cli():
  """A CLI for Video Camera Control"""
  pass


@cli.command()
@click.argument('power_level', default='off')
def power(power_level):
  import ArduinoController
  if power_level == 'on':
    ArduinoController.power(1)
  else:
    ArduinoController.power(0)


@cli.command()
@click.argument('zoom_mag', default=0.0)
def zoomin(zoom_mag):
  import ArduinoController
  if zoom_mag >= 0.0 and zoom_mag <= 100.0:
    ArduinoController.zoomin(zoom_mag)
  else:
    raise Exception('Not a valid input, value must be from 0 to 100.')


@cli.command()
@click.argument('zoom_mag', default=0.0)
def zoomout(zoom_mag):
  import ArduinoController
  if zoom_mag >= 0.0 and zoom_mag <= 100.0:
    ArduinoController.zoomout(zoom_mag)
  else:
    raise Exception('Not a valid input, value must be from 0 to 100.')

@cli.command()
@click.argument('record_time', default=0)
@click.argument('snaps', default=0)
def rc(record_time, snaps):
  import ArduinoController
  if record_time >= 0:
    ArduinoController.recordandcapture(record_time, snaps)
  else:
    raise Exception('Not a valid input, value must be positive.')


@cli.command()
@click.argument('level', default='off')
def transfer(level):
  import ArduinoController
  if level == 'on':
    ArduinoController.transfer(1)
    print('Ready to transfer data')
  elif level == 'off':
    ArduinoController.transfer(0)
  else:
    print('Not a valid input')


@cli.command()
def home():
  import ArduinoController
  ArduinoController.home()


@cli.command()
def format():
  import ArduinoController
  ArduinoController.format()


@cli.command()
def ft():
  import ArduinoController
  ArduinoController.ft()


@cli.command()
def move():
  import ArduinoController
  ArduinoController.move()


@cli.command()
def record():
  import ArduinoController
  ArduinoController.startrecord()
  print('Recording In Progress')


@cli.command()
def stop():
  import ArduinoController
  ArduinoController.stoprecord()
  print('Stopped Recording')


@cli.command()
def capture():
  import ArduinoController
  ArduinoController.capture()


@cli.command()
def save():
  import ArduinoController
  ArduinoController.save()


@cli.command()
def mount():
  import ArduinoController
  ArduinoController.mount()


@cli.command()
def rmlocal():
  import ArduinoController
  ArduinoController.rmlocal()


@cli.command()
@click.argument('camera', default=0.0)
def control(camera):
  import ArduinoController
  if camera >= 0.0 and camera <= 17.0:
    ArduinoController.control(camera)
  else:
    raise Exception('Not a valid input, value must be from 0 to 17.')

@cli.command()
@click.argument('exposure_amount', default=0)
def expos(exposure_amount):
  import ArduinoController
  if exposure_amount >= 0:
    print(exposure_amount)
    ArduinoController.expos(exposure_amount)
  else:
    raise Exception('Not a valid input, value must be positive.')

@cli.command()
@click.argument('exposure_amount', default=0)
def exneg(exposure_amount):
  import ArduinoController
  if exposure_amount >= 0:
    print(exposure_amount)
    ArduinoController.exneg(exposure_amount)
  else:
    raise Exception('Not a valid input, value must be positive.')

@cli.command()
def manex():
  import ArduinoController
  ArduinoController.manex()

@cli.command()
def steady():
  import ArduinoController
  ArduinoController.steady()

@cli.command()
def autoex():
  import ArduinoController
  ArduinoController.autoex()

if __name__ == '__main__':
  cli()
