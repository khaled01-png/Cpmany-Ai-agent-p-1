export const metadata = {
  title: "DevTork AI Agent",
  description: "AI employee for DevTork Studio",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
