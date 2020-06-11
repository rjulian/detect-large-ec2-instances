# detect-large-ec2-instances

Detects an ec2 instance being launched with a disallowed type.

## Usage

To use this rule either add it to your `reflex.yaml` configuration file:

```
rules:
  - detect-large-ec2-instances:
      version: latest
```

or add it directly to your Terraform:

```
...

module "detect-large-ec2-instances" {
  source           = "github.com/rjulian/detect-large-ec2-instances"
}

...
```

## License

This Reflex rule is made available under the MPL 2.0 license. For more information view
the [LICENSE](https://github.com/cloudmitigator/detect-large-ec2-instances/blob/master/LICENSE)
