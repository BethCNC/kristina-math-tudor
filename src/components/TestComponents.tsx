import { Button } from "./ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "./ui/card"
import { Input } from "./ui/input"
import { Badge } from "./ui/badge"
import { Alert, AlertDescription } from "./ui/alert"

export function TestComponents() {
  return (
    <div className="p-8 space-y-8">
      <div className="space-y-4">
        <h2 className="text-2xl font-bold text-[var(--color-text-primary)]">shadcn/ui Components with Your Design System</h2>
        
        {/* Button Variants */}
        <div className="space-y-4">
          <h3 className="text-lg font-semibold text-[var(--color-text-secondary)]">Button Variants</h3>
          <div className="flex flex-wrap gap-4">
            <Button variant="default">Default</Button>
            <Button variant="destructive">Destructive</Button>
            <Button variant="outline">Outline</Button>
            <Button variant="secondary">Secondary</Button>
            <Button variant="ghost">Ghost</Button>
            <Button variant="link">Link</Button>
          </div>
          
          <div className="flex flex-wrap gap-4">
            <Button size="sm">Small</Button>
            <Button size="default">Default</Button>
            <Button size="lg">Large</Button>
          </div>
        </div>

        {/* Card Component */}
        <div className="space-y-4">
          <h3 className="text-lg font-semibold text-[var(--color-text-secondary)]">Card Component</h3>
          <Card className="w-full max-w-md">
            <CardHeader>
              <CardTitle className="text-[var(--color-text-primary)]">Create Project</CardTitle>
              <CardDescription className="text-[var(--color-text-muted)]">
                Deploy your new project in one-click.
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="space-y-2">
                <label className="text-sm font-medium text-[var(--color-text-primary)]">Name</label>
                <Input placeholder="Name of your project" />
              </div>
              <Button className="w-full">Create Project</Button>
            </CardContent>
          </Card>
        </div>

        {/* Badge Component */}
        <div className="space-y-4">
          <h3 className="text-lg font-semibold text-[var(--color-text-secondary)]">Badge Component</h3>
          <div className="flex flex-wrap gap-2">
            <Badge variant="default">Default</Badge>
            <Badge variant="secondary">Secondary</Badge>
            <Badge variant="destructive">Destructive</Badge>
            <Badge variant="outline">Outline</Badge>
          </div>
        </div>

        {/* Alert Component */}
        <div className="space-y-4">
          <h3 className="text-lg font-semibold text-[var(--color-text-secondary)]">Alert Component</h3>
          <Alert>
            <AlertDescription>
              This is a default alert with your design system colors.
            </AlertDescription>
          </Alert>
        </div>
      </div>
    </div>
  )
}
