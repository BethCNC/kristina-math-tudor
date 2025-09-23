import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "src/lib/utils"

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 font-['Host_Grotesk']",
  {
    variants: {
      variant: {
        default: "bg-[var(--color-brand-default)] text-[var(--color-text-inverse-primary)] hover:bg-[var(--color-brand-default)]/90",
        destructive:
          "bg-[var(--color-danger-default)] text-[var(--color-text-inverse-primary)] hover:bg-[var(--color-danger-default)]/90",
        outline:
          "border border-[var(--color-border-secondary)] bg-[var(--color-background-default)] hover:bg-[var(--color-background-secondary)] hover:text-[var(--color-text-primary)]",
        secondary:
          "bg-[var(--color-background-secondary)] text-[var(--color-text-primary)] hover:bg-[var(--color-background-secondary)]/80",
        ghost: "hover:bg-[var(--color-background-secondary)] hover:text-[var(--color-text-primary)]",
        link: "text-[var(--color-text-primary)] underline-offset-4 hover:underline",
      },
      size: {
        default: "h-11 px-4 py-2.5 text-xl leading-[24px]",
        sm: "h-10 rounded-md px-3 text-lg",
        lg: "h-12 rounded-md px-8 text-xl",
        icon: "h-10 w-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button"
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    )
  }
)
Button.displayName = "Button"

export { Button, buttonVariants }
